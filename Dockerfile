ARG WRKDIR=/action

FROM python:3.9 AS builder
ARG WRKDIR
ADD . $WRKDIR
WORKDIR $WRKDIR
RUN pip install -r requirements.txt --target=$WRKDIR install

FROM gcr.io/distroless/python3-debian11
ARG WRKDIR
COPY --from=builder $WRKDIR $WRKDIR
WORKDIR $WRKDIR
ENV PYTHONPATH=${WRKDIR}
ENV API_URL="https://ms-oss-pytest-services-staging.digitalpfizer.com/api/v1/save-test-execution"
ENV GITHUB_TOKEN="GITHUB-ACTION-AUTH-TOKEN"
CMD ["/action/main.py"]
