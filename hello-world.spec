Summary: A simple program that prints hello
Name: hello-world
Version: 1.0.0
Release: 1
URL: https://example.com
Group: System
License: example # https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Software_License_List
Packager: Example Team
Requires: bash

%description
An example package containing a hello-world binary

%install
mkdir -p %{buildroot}/usr/bin/
cp ~/rpmbuild/SOURCES/hello-world %{buildroot}/usr/bin/hello-world

%files
/usr/bin/hello-world

%changelog
* Thu Jun 17 2021 alex <alex@earthly.dev>
- initial example
