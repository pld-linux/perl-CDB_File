#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	CDB_File - Perl extension for access to cdb databases
Summary(pl.UTF-8):	CDB_File - rozszerzenie Perla umożliwiające dostęp do baz cdb
Name:		perl-CDB_File
Version:	0.97
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CDB_File/CDB_File-%{version}.tar.gz
# Source0-md5:	22fd84f6b2176528001835eae706e66d
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
%attr(755,root,root) %{perl_vendorarch}/auto/CDB_File/CDB_File.so
%{_mandir}/man3/*
