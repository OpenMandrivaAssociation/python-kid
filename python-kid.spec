%define module	kid
%define name	python-%{module}
%define version	0.9.6
%define release	%mkrel 1

Name:		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:        A simple and pythonic XML template language
Group: 		Development/Python
License:        MIT
URL:            http://kid-templating.org/
Source0:        http://www.kid-templating.org/dist/%{version}/kid-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:      noarch
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-celementtree
BuildRequires:	python-elementtree
BuildRequires:	python-setuptools
Requires:       python-elementtree

%description
Kid is a simple Python based template language for generating and
transforming XML vocabularies. Kid was spawned as a result of a kinky love
triangle between XSLT, TAL, and PHP. We believe many of the best features
of these languages live on in Kid with much of the limitations and
complexity stamped out (well, eventually :).

Templates are compiled to native Python byte-code and may be imported and
used like normal Python modules.


%prep
%setup -q -n kid-%{version}
perl -pi -e 's/^(use_setuptools)/#$1/' setup.py
rm -f doc/#guide.txt#

%build
python setup.py build


%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%check
make clean
make test

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc doc/* examples


