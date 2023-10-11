FROM fedora:latest

# RUN adduser -D appuser


RUN dnf -y update \
    && dnf -y install rpmdevtools* \
        rpmlint \
        tree \
        git \
    && dnf clean all

RUN adduser appuser
USER appuser

RUN rpmdev-setuptree

USER root

# COPY hello.sh .
#COPY hello.spec .
#RUN mkdir hello-0.0.1
#RUN mv hello.sh hello-0.0.1
#RUN tar --create --file hello-0.0.1.tar.gz hello-0.0.1
#RUN mv hello-0.0.1.tar.gz /home/appuser/rpmbuild/SOURCES
#RUN mv hello.spec /home/appuser/rpmbuild/SPECS
## RUN mv hello-0.0.1
#RUN rm -rf hello-0.0.1
#USER appuser
#RUN rpmlint ~/rpmbuild/SPECS/hello.spec
#RUN rpmbuild -bs ~/rpmbuild/SPECS/hello.spec
#RUN rpmbuild -bb ~/rpmbuild/SPECS/hello.spec
#
#USER root
#RUN dnf install /home/appuser/rpmbuild/RPMS/noarch/hello-0.0.1-1.fc38.noarch.rpm -y


EXPOSE 80

CMD [ "/bin/bash" ]