%define module	kid
%define name	python-%{module}
%define version	0.9.6
%define release	4

Name:		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:        A simple and pythonic XML template language
Group: 		Development/Python
License:        MIT
URL:            https://kid-templating.org/
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

%files
%defattr(-,root,root)
%doc doc/* examples
%{_bindir}/*
%py_puresitedir/*


%changelog
* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 0.9.6-3mdv2011.0
+ Revision: 598277
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.9.6-3mdv2010.0
+ Revision: 442223
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.9.6-2mdv2009.1
+ Revision: 323754
- rebuild

* Fri Aug 15 2008 Michael Scherer <misc@mandriva.org> 0.9.6-1mdv2009.0
+ Revision: 272295
- new version
- correct url

* Thu Jul 10 2008 Michael Scherer <misc@mandriva.org> 0.9.5-2mdv2009.0
+ Revision: 233578
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 08 2007 Michael Scherer <misc@mandriva.org> 0.9.5-1mdv2008.0
+ Revision: 49753
- new version, remove patch1
- change url


* Fri Jan 12 2007 Olivier Blin <oblin@mandriva.com> 0.9.4-1mdv2007.0
+ Revision: 107891
- patch makefile to correctly run cElementTree test
- 0.9.4

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Rebuild against new python

  + Michael Scherer <misc@mandriva.org>
    - Import python-kid

* Fri Jan 06 2006 Michael Scherer <misc@mandriva.org> 0.8-2mdk
- Fix BuildRequires

* Fri Dec 09 2005 Michael Scherer <misc@mandriva.org> 0.8-1mdk
- New release 0.8
- do not use setuptools setuptools
- add documentation 
- add test

* Thu Jul 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.3-2mdk 
- used mkrel

* Fri Jul 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.3-1mdk 
- first mdk release, using spec file from Konstantin Ryabitsev <icon@linux.duke.edu>

