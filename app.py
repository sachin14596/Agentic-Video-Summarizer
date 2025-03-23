import streamlit as st 
from phi.agent import Agent 
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo 
from google.generativeai import upload_file, get_file
import google.generativeai as genai
import time
from pathlib import Path 
import mimetypes
import tempfile

from dotenv import load_dotenv
load_dotenv()

import os

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

#Page Configuration

st.set_page_config(
    page_title="Multimodal AI Agent - Video Summarizer",
    page_icon="Video",
    layout="wide"
)

st.title("Phidata Multimodal AI Video Summarizer Agent 🤖 🎥")
st.header("Powered by Gemini 2.0 Flash Exp")

st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True,
    )

#Initialize the Agent

multimodal_Agent=initialize_agent()

#File Uploader
video_file=st.file_uploader(
    "Upload a video file", type=['mp4','mov','avi'], help="Upload a video for AI Analysis"
)

if video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='mp4') as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name 
    
    st.video(video_path, format="video/mp4", start_time=0)

    user_query=st.text_area(
        "What insightes are you seeking from the video?",
        placeholder="Ask anything about the video content. The AI Agent will analyze and gather additional information",
        help="Provide specific questions or insights you want from the video"

    )

    if st.button("🔍 Analyze Video", key="analyze_video_button"):
        if not user_query:
            st.warning("Please enter a question or insigt to analyze the video")
        else:
            try:
                with st.spinner("Processing video and gathering insights..."):
                    # Upload and process video file
                    mime_type, _ = mimetypes.guess_type(video_path)
                    if not mime_type:
                        mime_type = "video/mp4"
                        processed_video = upload_file(video_path, mime_type=mime_type)
                    while processed_video.state.name=="PROCESSING":
                        time.sleep(1)
                        processed_video=get_file(processed_video.name)

                    # Prompt generation for analysis
                    analysis_prompt=(
                        f"""
                        Analyze the uploaded video for content and context.
                        Respond to the following query usnig video insights and supplementary web research
                        {user_query}

                        provide a detailed, user-friendly, and actionable response
                        """
                    )

                    # AI Agent Processing
                    response = multimodal_Agent.run(analysis_prompt, videos=[processed_video])

                # Display the result
                st.subheader("Analysis Result")
                st.markdown(response.content)

            except Exception as error:
                st.error(f"An error occurred during analysis: {error}")
            finally:
                # Clean up temporary video file
                  Path(video_path).unlink(missing_ok=True)
    else:
        st.info("Upload a video file to begin analysis")
    
    # Customize Text area height
    st.markdown(
        """
        <style>
        .stTextArea textarea {
            height: 100px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )