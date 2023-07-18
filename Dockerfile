ARG WRKDIR=/action

FROM python:3.9-alpine AS builder
ARG WRKDIR
ADD . $WRKDIR
WORKDIR $WRKDIR
RUN pip install -r requirements.txt --target=$WRKDIR install

FROM gcr.io/distroless/python3-debian11
ARG WRKDIR
COPY --from=builder $WRKDIR $WRKDIR
WORKDIR $WRKDIR
ENV PYTHONPATH=${WRKDIR}
CMD ["/action/main.py"]
