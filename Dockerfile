# Use an official Python runtime as a parent image (the base image):
FROM python:3.11-slim


# Install any needed packages specified in requirements. + clean unrelevant files to reduce image size
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-tk \
    tk \
    && rm -rf /var/lib/apt/lists* 


# All following commands will be executed in the /app directory, which will be created if it doesn't exist:
WORKDIR /app

# Install Python laibraries:
RUN pip install --no-cache-dir pandas

# Copy all the project files into the container at /app:
COPY . .

# Set environment variables for the game directory and the main game file:
ENV GAME_DIR=snake_game
ENV GAME_FILE=main.py

# Run the game when the container launches:
CMD ["sh", "-c", "cd /app/$GAME_DIR && python $GAME_FILE"]