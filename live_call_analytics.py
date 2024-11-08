from diagrams.aws.analytics import KinesisVideoStreams,KinesisDataStreams
from diagrams.aws.compute import Lambda
from diagrams.aws.ml import Transcribe, Comprehend,Lex,Kendra
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.onprem.database import Postgresql
from diagrams.onprem.inmemory import Redis
from diagrams import Diagram, Cluster


diagram_graph_attr = {
    "fontsize": "45",
    "bgcolor": "grey"
}

cluster_graph_attr={
    "bgcolor": ""
}


with Diagram(name="Live Call Analytics", filename="live_call_analytics_aws_arch",show=False):

    # Blocks Involved

    input_text_stream = KinesisDataStreams(label="AWS Kinesis Data Stream")
    with Cluster(label="Agent Assist Chatbot"):
        chatbot_handler = Lambda("AWS Lambda \n Chatbot Handler")
        chatbot = Lex(label="Agent Assist Chatbot")
        rag = Kendra(label="AWS Kendra - Vector Store")
    # knowledge_base_sources = #PDFs docs.
    # crm_sources = # Crm info

    with Cluster(label="Live Call Analytics (LCA)"):
        lca_handler = Lambda(label="AWS Lambda \n LCA Handler")
        sentiment_analysis = Comprehend(label="AWS Comprehend \n(Sentiment Analysis)")


    output_text_stream = Redis(label="Output Text Stream")

    # Interconnections

    # input_audio_stream >> audio_stream_handler >> [call_storage, event_storage,output_text_stream, transcription_service]
    # transcription_service >> audio_stream_handler