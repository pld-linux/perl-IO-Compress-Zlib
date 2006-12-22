#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Compress-Zlib
Summary:	Perl interface to read/write gzip and zip files/buffers
Summary(pl):	Perlowy interfejs do odczytu/zapisu plik�w/bufor�w gzip i zip
Name:		perl-IO-Compress-Zlib
Version:	2.001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	265c31ec11a220999b6b29d47e3baddc
URL:		http://search.cpan.org/dist/IO-Compress-Zlib/
%if %{with tests}
BuildRequires:	perl-Compress-Raw-Zlib
BuildRequires:	perl-IO-Compress-Base
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to allow reading and writing of
RFC 1950, 1951, 1952 (i.e. gzip) and zip files/buffers.

%description -l pl
Ten modu� udost�pnia perlowy interfejs pozwalaj�cy na odczyt i zapis
plik�w/bufor�w w formacie zgodnym z RFC 1950, 1951, 1952 (czyli gzip)
oraz zip.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/Compress/Adapter/Deflate.pm
%{perl_vendorlib}/IO/Compress/Adapter/Identity.pm
%{perl_vendorlib}/IO/Compress/Deflate.pm
%{perl_vendorlib}/IO/Compress/Gzip.pm
%{perl_vendorlib}/IO/Compress/RawDeflate.pm
%{perl_vendorlib}/IO/Compress/Zip.pm
%{perl_vendorlib}/IO/Compress/Gzip
%{perl_vendorlib}/IO/Compress/Zip
%{perl_vendorlib}/IO/Compress/Zlib
%{perl_vendorlib}/IO/Uncompress/Adapter/Identity.pm
%{perl_vendorlib}/IO/Uncompress/Adapter/Inflate.pm
%{perl_vendorlib}/IO/Uncompress/AnyInflate.pm
%{perl_vendorlib}/IO/Uncompress/Gunzip.pm
%{perl_vendorlib}/IO/Uncompress/Inflate.pm
%{perl_vendorlib}/IO/Uncompress/RawInflate.pm
%{perl_vendorlib}/IO/Uncompress/Unzip.pm
%{_mandir}/man3/IO::*
%{_examplesdir}/%{name}-%{version}
