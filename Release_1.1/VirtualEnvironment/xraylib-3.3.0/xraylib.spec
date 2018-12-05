#Copyright (c) 2009-2014, Tom Schoonjans
#All rights reserved.

#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#    * The names of the contributors may not be used to endorse or promote products derived from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY Tom Schoonjans ''AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Tom Schoonjans BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.




%define luaver 
%define lualibdir %{_libdir}/lua/%{luaver}

%define rubydir 
%define perldir ${exec_prefix}/lib/perl5/site_perl/5.26.1/x86_64-linux-gnu-thread-multi
%define perllibdir ${exec_prefix}/lib/perl5/site_perl/5.26.1/x86_64-linux-gnu-thread-multi/auto/xraylib

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name: xraylib
Version: 3.3.0	
Release:	1%{?dist}
Summary: A library for X-ray matter interactions cross sections for X-ray fluorescence applications: core C library
Group:	 Applications/Engineering and Scientific	
License: BSD 
Packager: Tom.Schoonjans <Tom.Schoonjans@me.com>
URL: http://github.com/tschoonj/xraylib
Source: xraylib-%{version}.tar.gz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: gcc glibc glibc-headers glibc-devel gcc-gfortran >= 4.3.0 python-devel swig lua-devel ruby-devel perl-devel
BuildRequires: Cython numpy 
%if 0%{?fedora}
#only fedora has default support for python3 nowadays...
BuildRequires: python3-Cython python3-numpy python3-devel
%endif

%description
Quantitative estimate of elemental composition by spectroscopic and imaging techniques using X-ray fluorescence requires the availability of accurate data of X-ray interaction with matter. Although a wide number of computer codes and data sets are reported in literature, none of them is presented in the form of freely available library functions which can be easily included in software applications for X-ray fluorescence. This work presents a compilation of data sets from different published works and an xraylib interface in the form of callable functions. Although the target applications are on X-ray fluorescence, cross sections of interactions like photoionization, coherent scattering and Compton scattering, as well as form factors and anomalous scattering functions, are also available.

This rpm package provides only the core C library.

%package devel
Summary:A library for X-ray matter interactions cross sections for X-ray fluorescence applications: development package
Requires: glibc-devel glibc-headers pkgconfig

%description devel
Quantitative estimate of elemental composition by spectroscopic and imaging techniques using X-ray fluorescence requires the availability of accurate data of X-ray interaction with matter. Although a wide number of computer codes and data sets are reported in literature, none of them is presented in the form of freely available library functions which can be easily included in software applications for X-ray fluorescence. This work presents a compilation of data sets from different published works and an xraylib interface in the form of callable functions. Although the target applications are on X-ray fluorescence, cross sections of interactions like photoionization, coherent scattering and Compton scattering, as well as form factors and anomalous scattering functions, are also available.

This rpm package provides the necessary libraries, headers etc to start your own xraylib based development.

%package fortran
Summary:A library for X-ray matter interactions cross sections for X-ray fluorescence applications: fortran bindings
Requires: xraylib pkgconfig libgfortran >= 4.3.0 gcc-gfortran >= 4.3.0

%description fortran 
Quantitative estimate of elemental composition by spectroscopic and imaging techniques using X-ray fluorescence requires the availability of accurate data of X-ray interaction with matter. Although a wide number of computer codes and data sets are reported in literature, none of them is presented in the form of freely available library functions which can be easily included in software applications for X-ray fluorescence. This work presents a compilation of data sets from different published works and an xraylib interface in the form of callable functions. Although the target applications are on X-ray fluorescence, cross sections of interactions like photoionization, coherent scattering and Compton scattering, as well as form factors and anomalous scattering functions, are also available.

This rpm package provides the fortran 2003 bindings of xraylib.

%if 0%{?rhel} && 0%{?rhel} > 6
%package python
Summary:A library for X-ray matter interactions cross sections for X-ray fluorescence applications: python bindings
Requires: python xraylib numpy
%if 0%{?fedora}
Requires: python3 python3-numpy
%endif

%description python
Quantitative estimate of elemental composition by spectroscopic and imaging techniques using X-ray fluorescence requires the availability of accurate data of X-ray interaction with matter. Although a wide number of computer codes and data sets are reported in literature, none of them is presented in the form of freely available library functions which can be easily included in software applications for X-ray fluorescence. This work presents a compilation of data sets from different published works and an xraylib interface in the form of callable functions. Although the target applications are on X-ray fluorescence, cross sections of interactions like photoionization, coherent scattering and Compton scattering, as well as form factors and anomalous scattering functions, are also available. 

This rpm package provides the python bindings of xraylib and a command utility.

%endif

%package lua
Summary:A library for X-ray matter interactions cross sections for X-ray fluorescence applications: lua bindings
Requires: lua xraylib

%description lua
Quantitative estimate of elemental composition by spectroscopic and imaging techniques using X-ray fluorescence requires the availability of accurate data of X-ray interaction with matter. Although a wide number of computer codes and data sets are reported in literature, none of them is presented in the form of freely available library functions which can be easily included in software applications for X-ray fluorescence. This work presents a compilation of data sets from different published works and an xraylib interface in the form of callable functions. Although the target applications are on X-ray fluorescence, cross sections of interactions like photoionization, coherent scattering and Compton scattering, as well as form factors and anomalous scattering functions, are also available. 

This rpm package provides the lua bindings of xraylib.

%package ruby
Summary:A library for X-ray matter interactions cross sections for X-ray fluorescence applications: ruby bindings
Requires: ruby xraylib

%description ruby
Quantitative estimate of elemental composition by spectroscopic and imaging techniques using X-ray fluorescence requires the availability of accurate data of X-ray interaction with matter. Although a wide number of computer codes and data sets are reported in literature, none of them is presented in the form of freely available library functions which can be easily included in software applications for X-ray fluorescence. This work presents a compilation of data sets from different published works and an xraylib interface in the form of callable functions. Although the target applications are on X-ray fluorescence, cross sections of interactions like photoionization, coherent scattering and Compton scattering, as well as form factors and anomalous scattering functions, are also available. 

This rpm package provides the ruby bindings of xraylib.

%package perl
Summary:A library for X-ray matter interactions cross sections for X-ray fluorescence applications: perl bindings
Requires: perl xraylib

%description perl 
Quantitative estimate of elemental composition by spectroscopic and imaging techniques using X-ray fluorescence requires the availability of accurate data of X-ray interaction with matter. Although a wide number of computer codes and data sets are reported in literature, none of them is presented in the form of freely available library functions which can be easily included in software applications for X-ray fluorescence. This work presents a compilation of data sets from different published works and an xraylib interface in the form of callable functions. Although the target applications are on X-ray fluorescence, cross sections of interactions like photoionization, coherent scattering and Compton scattering, as well as form factors and anomalous scattering functions, are also available. 

This rpm package provides the perl bindings of xraylib.


%prep

%setup -q
pushd ..
cp -r xraylib-%{version} xraylib-%{version}-python2
%if 0%{?fedora}
cp -r xraylib-%{version} xraylib-%{version}-python3
%endif
popd

%build
#first run WITHOUT python
%configure --disable-java --disable-idl --enable-fortran2003 --disable-python --enable-lua --enable-ruby --enable-ruby-integration --enable-perl-integration --enable-perl --disable-python-numpy FC=gfortran 
#necessary to fix rpath issues during rpmbuild
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%if 0%{?rhel} && 0%{?rhel} > 6
#python2
pushd ../xraylib-%{version}-python2
%configure --disable-java --disable-idl --disable-fortran2003 --enable-python --disable-lua --disable-ruby --disable-perl --enable-python-numpy PYTHON=%{__python2} CYTHON=/usr/bin/cython
popd

#python3
%if 0%{?fedora}
pushd ../xraylib-%{version}-python3
%configure --disable-java --disable-idl --disable-fortran2003 --enable-python --disable-lua --disable-ruby --disable-perl --enable-python-numpy PYTHON=%{__python3} CYTHON=/usr/bin/cython3
popd
%endif
%endif

make 

%if 0%{?rhel} && 0%{?rhel} > 6
mv ../xraylib-%{version}-python2/python python2
%if 0%{?fedora}
mv ../xraylib-%{version}-python3/python python3
%endif

cd python2
make
cd ..
%if 0%{?fedora}
cd python3
make
cd ..
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%if 0%{?rhel} && 0%{?rhel} > 6
cd python2
make install DESTDIR=$RPM_BUILD_ROOT
cd ..
%if 0%{?fedora}
cd python3
make install DESTDIR=$RPM_BUILD_ROOT
cd ..
%endif
%else
rm -f $RPM_BUILD_ROOT%{_prefix}/share/xraylib/*.txt
%endif

libtool --finish $RPM_BUILD_ROOT%{_libdir}
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{lualibdir}/*.la
rm -f $RPM_BUILD_ROOT%{rubydir}/*.la
rm -f $RPM_BUILD_ROOT%{perllibdir}/*.la
%if 0%{?rhel} && 0%{?rhel} > 6
rm -f $RPM_BUILD_ROOT%{python2_sitearch}/*.la
%if 0%{?fedora}
rm -f $RPM_BUILD_ROOT%{python3_sitearch}/*.la
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)

%{_libdir}/libxrl.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libxrl.so
%{_libdir}/libxrl.a
%{_includedir}/xraylib/*.h
%{_libdir}/pkgconfig/libxrl.pc

%files fortran
%defattr(-,root,root)

%{_libdir}/libxrlf03.so.*
%{_libdir}/libxrlf03.so
%{_libdir}/libxrlf03.a
%{_includedir}/xraylib/*.mod
%{_libdir}/pkgconfig/libxrlf03.pc

%if 0%{?rhel} && 0%{?rhel} > 6
%files python
%defattr(-,root,root)
%{_bindir}/xraylib
%{python2_sitelib}/xraylib.py*
%{python2_sitelib}/xrayhelp.py*
%{python2_sitelib}/xraymessages.py*
%{python2_sitearch}/_xraylib.*
%{python2_sitearch}/xraylib_np.*
%if 0%{?fedora}
%{python3_sitelib}/xraylib.py*
%{python3_sitelib}/xrayhelp.py*
%{python3_sitelib}/xraymessages.py*
%{python3_sitelib}/__pycache__/*
%{python3_sitearch}/_xraylib.*
%{python3_sitearch}/xraylib_np.*
%endif
%{_prefix}/share/xraylib/*.txt
%endif

%files lua
%defattr(-,root,root)
%{lualibdir}/*

%files ruby
%defattr(-,root,root)
%{rubydir}/*

%files perl
%defattr(-,root,root)
%{perldir}/xraylib.pm
%{perllibdir}/xraylib.so

%changelog
* Mon Sep 18 2017 Tom Schoonjans
- Remove python bindings for RHEL6
* Wed Nov 23 2016 Tom Schoonjans
- Remove support for IDL

* Wed Dec 10 2014 Tom Schoonjans
- Support added for python3

* Tue Jun 3 2014 Tom Schoonjans
- Added python-numpy bindings

* Mon Jun 24 2013 Tom Schoonjans
- Added perl bindings
- Slight change of python bindings

* Tue Jun 18 2013 Tom Schoonjans
- Added ruby bindings

* Thu Aug 23 2012 Tom Schoonjans
- Added lua bindings

* Wed May 18 2011 Tom Schoonjans
- Added xraylib_auger.pro to idl package

* Mon Mar 22 2010 Tom Schoonjans
- Python files modified so they don't contain java files

* Mon Mar 08 2010 Tom Schoonjans
- Added IDL bindings
- ldconfig line

* Thu Aug 20 2009 Tom Schoonjans
- Initial spec file. Perl bindings not included.
