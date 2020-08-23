FROM python

MAINTAINER Adrian Raiser <adrian.raiser10@web.de>

RUN apt-get --yes update
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install --yes ca-certificates-java
RUN apt-get install --yes openjdk-11-jdk junit junit4 && apt-get clean

# Python-Stuff
RUN apt-get update -y
RUN apt-get install --yes python3            python               && apt-get clean
RUN apt-get install --yes                    ipython              && apt-get clean
RUN apt-get install --yes python3-requests                        && apt-get clean
RUN apt-get install --yes python3-pip                             && apt-get clean
RUN apt-get install --yes python3-six        python-six           && apt-get clean
RUN apt-get install --yes python3-responses                       && apt-get clean
RUN apt-get install --yes python3-xlrd                            && apt-get clean
RUN apt-get install --yes python3-simplejson python-simplejson    && apt-get clean


RUN apt-get install --yes ghc libghc-test-framework-dev libghc-test-framework-hunit-dev libghc-test-framework-quickcheck2-dev

WORKDIR /server

COPY src Praktomat/src/
COPY media Praktomat/media/
COPY requirements.txt Praktomat/
#COPY runserver.sh .

#RUN chmod +x ./runserver.sh

RUN mkdir PraktomatSupport

RUN pip install -r Praktomat/requirements.txt

RUN Praktomat/src/manage-local.py collectstatic --noinput --link
RUN Praktomat/src/manage-local.py migrate --noinput

ENTRYPOINT ["Praktomat/src/manage-local.py", "runserver"]