%include	/usr/lib/rpm/macros.perl
Summary:	CDB_File perl module
Summary(pl):	Modu³ perla CDB_File
Name:		perl-CDB_File
Version:	0.86
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CDB_File/CDB_File-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CDB_File - perl interface to CDB.

%description -l pl
CDB_File - interfejs do CDB dla perla.

%prep
%setup -q -n CDB_File-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ACKNOWLEDGE CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/CDB_File.pm
%dir %{perl_sitearch}/auto/CDB_File
%{perl_sitearch}/auto/CDB_File/CDB_File.bs
%attr(755,root,root) %{perl_sitearch}/auto/CDB_File/CDB_File.so
%{_mandir}/man3/*
