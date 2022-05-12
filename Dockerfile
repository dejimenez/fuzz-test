FROM alpine as clone

RUN apk add --no-cache git
RUN git clone https://github.com/microsoft/restler-fuzzer.git


FROM --platform=linux/x86_64/v8 mcr.microsoft.com/dotnet/sdk:5.0-alpine as builder

RUN apk add --no-cache python3 py3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY --from=clone /restler-fuzzer/src ./src
COPY --from=clone /restler-fuzzer/restler ./restler
COPY --from=clone /restler-fuzzer/build-restler.py .

RUN python3 build-restler.py --dest_dir /build

RUN python3 -m compileall -b /build/engine


FROM --platform=linux/x86_64/v8 mcr.microsoft.com/dotnet/aspnet:5.0-alpine as target

WORKDIR /fuzz

COPY requirements.txt .

RUN apk update && apk upgrade && \
    apk add --no-cache python3 py3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps postgresql-dev python3-dev gcc musl-dev libc-dev make g++ python3-dev libffi-dev openssl-dev && \
    pip3 install --no-cache-dir --upgrade -r requirements.txt && \
    apk del .build-deps gcc musl-dev g++ python3-dev libffi-dev openssl-dev postgresql-dev python3-dev

COPY --from=builder /build /fuzz/restler

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app"]
 