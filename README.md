# 🎙️ AI-Powered Meeting Summarization System

This project is an AI-powered web application that automatically summarizes audio and video recordings of meetings. It leverages CrewAI to orchestrate the transcription and summarization process, extracting key action items, sentiments, and generating concise summaries for insightful analysis.

---

## Demonstration Video

Here is the text that I am using in the demo video:

"Good morning, everyone. Thank you for joining today's meeting. Let's begin with a quick update on our current projects.

First, regarding the E-Commerce Platform, the development team has successfully integrated the payment gateway, and initial testing shows smooth transactions. However, we still need to refine the user authentication process to enhance security and reduce checkout friction. John, can you ensure the security review is completed by Friday?

Next, on the AI-powered Customer Support System, we've made good progress with chatbot training. The model now responds to 80% of customer queries correctly. However, there are still some gaps in handling complex refund-related questions. Sarah, please coordinate with the support team to gather more training data. We need to improve this by next week.

Now, moving on to Marketing and Outreach, our latest campaign has increased website traffic by 25% in the last month. However, conversions remain lower than expected. Mike, let's analyze user behavior data and suggest potential improvements to the landing pages."

[Click Here](https://www.loom.com/share/2436f6374e974afdbc80e0c90ab4d3a7)  to check out if meeting is properly summarized or not. 


## 🌟 Key Features

*   **Automatic Summarization:** Generates summaries of meeting recordings from audio or video input.
*   **Action Item Extraction:** Identifies and extracts key action items discussed during the meeting.
*   **Sentiment Analysis:** Analyzes the sentiment expressed in the meeting, providing insights into the overall tone.
*   **Audio/Video Support:** Processes both audio and video files.
*   **AI-Driven:** Powered by AI through CrewAI agents and flows.
*   **Transcription Integration:** Integrates with Azure OpenAI Whisper API for accurate audio-to-text conversion.
*   **Scalable Design:** Built for scalability to handle large volumes of recordings.
*   **Maintainable Architecture:** Employs best practices for AI-driven automation and workflow optimization.

---

## ⚙️ How It Works

The system uses a sequential design pattern:

  **Transcription:** The audio/video file is sent to the Azure OpenAI Whisper API for speech-to-text conversion.

  **Summarization:** The transcribed text is processed by CrewAI flows and agents. These extract key information (action items, sentiment) and generate a concise summary.

  **Output:** The summary, action items, and sentiment analysis are presented to the user.

---

## 🛠️ Technologies Used

*   **AI Workflow Orchestration:** CrewAI
*   **Transcription:** Azure OpenAI Whisper API
*   **Programming Languages:** Python
*   **Tools:** LangChain, CrewAI Toolkit, LlamaIndex

---

## 🚀 Installation



```bash
Example setup steps:

1. Clone the repository

   git clone <your_repository_url>

2. Navigate to the project directory

   cd Audio-text-summarize/

3. Ensure you have Python >=3.10 <3.13 installed on your system.

   pip install uv

4. Create a .env file in your project folder and add the following configuration variables:

   OPENAI_API_KEY = <key>

   WHISPER_API_KEY = <key>
   
   WHISPER_DEPLOYMENT_NAME = <deployment>


```
## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
crewai run
```
Now you will be getting a report.md file as your output file.
