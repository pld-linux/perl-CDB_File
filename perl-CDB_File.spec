#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
Summary:	CDB_File Perl module
Summary(pl):	Modu³ Perla CDB_File
Name:		perl-CDB_File
Version:	0.94
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CDB_File/CDB_File-%{version}.tar.gz
# Source0-md5:	3ff21ab85d0b61e2449ee5bfcc7584af
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CDB_File - Perl interface to CDB.

%description -l pl
CDB_File - interfejs do CDB dla Perla.

%prep
%setup -q -n CDB_File-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ACKNOWLEDGE CHANGES
%{perl_vendorarch}/CDB_File.pm
%dir %{perl_vendorarch}/auto/CDB_File
%{perl_vendorarch}/auto/CDB_File/CDB_File.bs
%attr(755,root,root) %{perl_vendorarch}/auto/CDB_File/CDB_File.so
%{_mandir}/man3/*
