Summary:	It's a gtk interface to mysql/postgresql databases
Name:		dbui
Version:	0.4.0
Release:	1
License:	GPL
Group:		Applications/Databases/Interfaces
Source0:	http://spyder.virtualbeer.net/dbui/%{name}-%{version}.tar.gz
URL:		http://spyder.virtualbeer.net/dbui/
BuildRequires:	gtk+-devel
BuildRequires:	mysql-devel
# BuildRequires:	postgresql-devel
Requires:	gtk+
Requires:	mysql-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix /usr/X11R6
%define         _mandir %{_prefix}/man

%description
Its a gtk interface to mysql databases. You might say a database editor. Its
still in its very early stages but you can fully search,update, add, and delete
any mysql databas. 

%package mysql
Summary:	dbui linked with mysql 
Requires: dbui = %{version}
Group:		Applications/Databases/Interfaces

%description mysql
dbui linked with mysql 

%package postgresql
Summary:	dbui linked with postgresql 
Requires: dbui = %{version}
Group:		Applications/Databases/Interfaces

%description postgresql
dbui linked with postgresql.
due to incompatibility with latest postgres libraries it doesn't compile
correctly

%prep
%setup  -q

%build
%{__make} -f Makefile.mysql
mv dbui dbui.mysql
# %{__make} -f Makefile.postgres
# mv dbui dbui.postgresql

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}

cp dbui.mysql $RPM_BUILD_ROOT/%{_bindir}
# cp dbui.postgresql $RPM_BUILD_ROOT/bin

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%files mysql
%attr(755,root,root) %{_bindir}/dbui.mysql

%files postgresql
# %attr(755,root,root) %{_bindir}/dbui.postgresql
