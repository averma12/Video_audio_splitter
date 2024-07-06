from setuptools import setup, find_packages

setup(
    name="video_audio_splitter",
    version="0.1.0",
    description="Download and chunk Loom, Zoom, and YouTube videos into audio files",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/video_audio_splitter",  # Update with your URL
    packages=find_packages(),
    install_requires=[
        "requests",
        "moviepy",
        "pydub",
        "yt-dlp"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
