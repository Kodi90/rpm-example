FROM centos:latest

#COPY ./hello.spec ./hello.spec
RUN ls
RUN cd /etc/yum.repos.d/ \
    && sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* \
    && sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* \
    && yum update -y \
    && yum install -y createrepo rpm-build rpm-sign wget gcc python3 yum-utils tree

RUN mkdir -p ~/example/hello-world-program
RUN echo '#include <stdio.h> \
    int main() { \
        printf("Hello World!\\n"); \
        return 0; \
    }' | gcc -o ~/example/hello-world-program/hello-world -x c -

RUN mkdir -p ~/example/rpm-work-dir
RUN cd ~/example/rpm-work-dir

RUN cd ~/example/rpm-work-dir

RUN echo "Summary: A simple program that prints hello \
    Name: hello-world \
    Version: 1.0.0 \
    Release: 1 \
    URL: https://example.com \
    Group: System \
    License: example # https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Software_License_List \
    Packager: Example Team \
    Requires: bash \
    BuildRoot: ~/example/rpm-work-dir # this should be replaced with your working directory where the spec is saved \
    \
    %description \
    An example package containing a hello-world binary \
    \
    %install \
    mkdir -p %{buildroot}/usr/bin/ \
    cp ~/example/hello-world-program/hello-world %{buildroot}/usr/bin/hello-world \
    \
    %files \
    /usr/bin/hello-world \
    \
    %changelog \
    * Thu Jun 17 2021 alex <alex@earthly.dev> \
    - initial example \
    " > hello-world.spec

RUN rpmbuild --target "x86_64" -bb hello-world.spec

#RUN #rpmdev-setuptree

#RUN #tree

#RUN tree
#RUN tree

CMD [ "/bin/bash" ]