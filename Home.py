#!/usr/bin/env python3
"""
Main analyzef1 script
"""

import logging
from pathlib import Path
from typing import Any, List

import streamlit as st

# from utils import set_page_config
import utils

logger = logging.getLogger(__name__)

LOGFORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOGFORMAT)


def main() -> None:
    utils.set_page_config()
    logger.info("Showing Home Page")
    st.title("F1InsightX 🏎️")

    # col1, col2 = st.columns([2, 2])
    # st.image(f"{Path().resolve()}/images/background/backgroundcrop.jpeg")
    # col1.image("C:/Users/Alok Sharma/Downloads/pexels-alejandro-barrón-96715.jpg")

    # col2.markdown("For all the **F1** nerds.")
    st.markdown("Get ready to experience Formula 1 like never before with **F1InsightX!**")
    st.divider()

    st.markdown("🏎️ Welcome to F1InsightX: Your Ultimate Formula 1 Telemetry Companion! 🚀")

    st.markdown("F1InsightX is a cutting-edge platform that brings the exhilarating world of Formula 1 closer to you. Dive into the heart of the races with our powerful telemetry analysis tool that provides a comprehensive view of driver performance, race strategies, and historical data. Whether you're a seasoned F1 enthusiast or new to the sport, F1InsightX is your go-to hub for gaining deeper insights into the dynamics of each race.")

    st.markdown("📈 Discover real-time telemetry comparisons between drivers, explore intricate race strategies, and access historical standings with just a few clicks. Our user-friendly interface ensures a seamless experience, allowing you to unravel the intricacies of Formula 1 sessions and strategies effortlessly.")

    st.markdown("🏁 Join us on this exciting journey as we unlock the hidden facets of Formula 1 through data-driven insights. F1InsightX is more than just a tool; it's your passport to understanding the science behind the speed, strategy, and spectacle that is Formula 1.")


    # st.image("C:/Users/Alok Sharma/Downloads/New folder (3)/prof1/analyzef1/images/background/backgroundcrop.jpeg")
    # st.image("C:/Users/Alok Sharma/Downloads/pexels-alejandro-barrón-96715.jpg")


    st.divider()
    st.subheader("Event Schedule")
    st.markdown(
        f"Display current race season. Next, Upcoming and Past events with session times."
    )
    st.subheader("Analyze Session")
    st.markdown(
        f"Analyze all previous sessions up to **2018**. If the session has just ended, the data should be available a few minutes later."
    )
    st.subheader("Leaderboard")
    st.markdown(f"Driver and constructor standings up to **2005**.")
    st.divider()


if __name__ == "__main__":
    main()
