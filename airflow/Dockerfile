FROM apache/airflow:2.10.2

ENV AIRFLOW_HOME=/opt/airflow

USER root

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Setup for Google Cloud SDK
ARG CLOUD_SDK_VERSION=495.0.0
ENV GCLOUD_HOME=/home/google-cloud-sdk
ENV PATH="${GCLOUD_HOME}/bin/:${PATH}"
USER root
RUN DOWNLOAD_URL="https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz" \
    && TMP_DIR="$(mktemp -d)" \
    && curl -fL "${DOWNLOAD_URL}" --output "${TMP_DIR}/google-cloud-sdk.tar.gz" \
    && mkdir -p "${GCLOUD_HOME}" \
    && tar xzf "${TMP_DIR}/google-cloud-sdk.tar.gz" -C "${GCLOUD_HOME}" --strip-components=1 \
    && "${GCLOUD_HOME}/install.sh" --bash-completion=false --path-update=false --usage-reporting=false --quiet \
    && rm -rf "${TMP_DIR}" \
    && gcloud --version

# Set working directory
WORKDIR $AIRFLOW_HOME

COPY scripts /opt/airflow/scripts
RUN chmod +x /opt/airflow/scripts/etrypoint.sh

# Switch to airflow user
USER $AIRFLOW_UID

