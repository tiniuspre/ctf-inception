from random import random

from flask import Flask, render_template, request, redirect, url_for, flash
from manager import CTFManager

app = Flask(__name__)
app.secret_key = "".join([chr(int(random() * 255)) for _ in range(32)])

manager = CTFManager()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check_container', methods=['POST'])
def check_container():
    participant = request.form.get('participant')

    if not participant:
        flash('Participant name is required', 'error')
        return redirect(url_for('index'))

    # Check if container exists, if not, create it
    container = manager._validate_participant(participant)
    if not container:
        container = manager.create_container(participant)

    return render_template('participant_container.html', container=container, participant=participant)


@app.route('/stop_container/<participant>', methods=['POST'])
def stop_container(participant):
    container = manager._validate_participant(participant)
    if container:
        try:
            container.stop()
            manager._release_port(container.port)
            del manager.running_containers[participant]
            flash(f"Container for {participant} stopped successfully", 'success')
        except Exception as e:
            flash(f"Error: {str(e)}", 'error')
    else:
        flash(f"No container found for {participant}", 'error')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=False)
