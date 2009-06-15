#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	CDB_File - Perl extension for access to cdb databases
Summary(pl.UTF-8):	CDB_File - rozszerzenie Perla umożliwiające dostęp do baz cdb
Name:		perl-CDB_File
Version:	0.96
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CDB_File/CDB_File-%{version}.tar.gz
# Source0-md5:	898ed12e7548930f178dba5ec4a193d3
URL:		http://search.cpan.org/dist/CDB_File/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CDB_File is a module which provides a Perl interface to Dan Berstein's
cdb package. cdb is a fast, reliable, lightweight package for creating
and reading constant databases.

%description -l pl.UTF-8
CDB_File jest modułem stanowiącym interfejs perlowy do pakietu cdb
Dana Bersteina. cdb jest szybkim, niezawodnym, lekkim pakietem do
odczytu i tworzenia stałych baz danych. 

%prep
%setup -q -n CDB_File-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
