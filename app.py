import os
from flask import Flask, render_template, request

from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    download_link = None

    if request.method == 'POST':
        video_url = request.form['video_url']

        try:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            download_path = os.path.join('downloads', f'{yt.title}.mp4')
            stream.download(output_path=download_path)
            download_link = download_path

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"

    return render_template('index.html', download_link=download_link)

if __name__ == '__main__':
    app.run(debug=True)
