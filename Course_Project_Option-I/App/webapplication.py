from flask import Flask, render_template

app = Flask(__name__)


def buildHtml(link, text):
   return "<a href='" + link + "'>" + text + "</a><br><br>"

@app.route("/")
def serve():
   services = []
   services.append(buildHtml("http://34.70.112.6:9870", "1. Apache Hadoop"))
   services.append(buildHtml("http://35.222.32.28", "2. Apache Spark"))
   services.append(buildHtml("http://35.224.125.170/?token=a0f66646fbbdf2e4dc0df562a434f052196e61765406b745", "3. Jupyter Notebook"))
   services.append(buildHtml("http://34.71.156.75", "4. SonarQube and SonarScanner"))
   instruction = "<h1>Big Data Processing Application</h1>" + "<p>Please select a service</p>"
   for service in services:
      instruction += service
   return instruction


if __name__ == '__main__':
   app.run(host='0.0.0.0')