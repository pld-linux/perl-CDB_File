%include	/usr/lib/rpm/macros.perl
Summary:	CDB_File perl module
Summary(pl):	Modu³ perla CDB_File
Name:		perl-CDB_File
Version:	0.7
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module//CDB_File-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
CDB_File - perl interface to CDB. 

%description -l pl
CDB_File - interfejs do CDB dla perla.

%prep
%setup -q -n CDB_File-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/CDB_File/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/CDB_File
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README ACKNOWLEDGE CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ACKNOWLEDGE,CHANGES}.gz

%{perl_sitearch}/CDB_File.pm

%dir %{perl_sitearch}/auto/CDB_File
%{perl_sitearch}/auto/CDB_File/.packlist
%{perl_sitearch}/auto/CDB_File/CDB_File.bs
%{perl_sitearch}/auto/CDB_File/autosplit.ix
%{perl_sitearch}/auto/CDB_File/multi_get.al
%attr(755,root,root) %{perl_sitearch}/auto/CDB_File/CDB_File.so

%{_mandir}/man3/*
