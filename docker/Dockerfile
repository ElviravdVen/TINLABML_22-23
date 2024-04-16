ARG BASE_CONTAINER=continuumio/miniconda3:23.3.1-0

FROM $BASE_CONTAINER

# Environment variables
ENV NB_USER="student"

LABEL MAINTAINER="Jeroen Boogaard <j.a.boogaard@hr.nl>"

# Root operations

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y gcc

# Set Timezone
RUN apt-get install tzdata \
    && cp /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime \
    && echo "Europe/Amsterdam" >  /etc/timezone

# Add non-root user and add directory app
RUN useradd -m ${NB_USER} 

# Add Python requirements with conda
RUN conda install conda=23.3.1 \
    && conda update --all

RUN conda install conda=23.5.0 \ 
    && conda install -y -c conda-forge numpy pandas pathlib pypickle scikit-learn \
    && conda install -y -c esrf-bcu ptpython \
    && conda install -y -c pytorch pytorch

# Switch to non-root user
USER ${NB_USER}

# Non-root operations

WORKDIR /home/${NB_USER}

# Add Python requirements with pip
ENV PATH=$PATH:/home/${NB_USER}/.local/bin
RUN pip install --upgrade pip tensorflow

ENTRYPOINT ["ptpython"]