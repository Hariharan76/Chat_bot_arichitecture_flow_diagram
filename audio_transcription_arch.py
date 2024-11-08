from diagrams.aws.analytics import KinesisVideoStreams,KinesisDataStreams
from diagrams.aws.compute import Lambda
from diagrams.aws.ml import Transcribe
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.onprem.database import Postgresql
from diagrams import Diagram, Cluster

diagram_graph_attr = {
    "fontsize": "45",
    "bgcolor": "grey"
}

cluster_graph_attr={
    "bgcolor": ""
}


with Diagram(name="Audio Transcription", filename="audio_transcription_aws_arch",show=False):

    # Blocks Involved

    input_audio_stream = KinesisVideoStreams(label="Input Audio Stream")
    with Cluster(label="Real time transcription"):
        audio_stream_handler = Lambda(label="Audio Stream \n Handler")
        transcription_service = Transcribe(label="Transcribe")
        call_storage = SimpleStorageServiceS3(label="Audio and Text \n Storage")
        event_storage = Postgresql(label="Call Events\nStorage")
    output_text_stream = KinesisDataStreams(label="Output Text Stream")

    # Interconnections

    input_audio_stream >> audio_stream_handler >> [call_storage, event_storage,output_text_stream, transcription_service]
    transcription_service >> audio_stream_handler


