%include	/usr/lib/rpm/macros.perl
Summary:	CDB_File perl module
Summary(pl):	Modu� perla CDB_File
Name:		perl-CDB_File
Version:	0.92
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CDB_File/CDB_File-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CDB_File - perl interface to CDB.

%description -l pl
CDB_File - interfejs do CDB dla perla.

%prep
%setup -q -n CDB_File-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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