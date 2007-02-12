Summary:	It's a GTK+ interface to MySQL/PostgreSQL databases
Summary(pl.UTF-8):   Interfejs GTK+ do baz danych MySQL/PostgreSQL
Name:		dbui
Version:	0.4.0
Release:	4
License:	GPL
Group:		Applications/Databases/Interfaces
Source0:	http://spyder.virtualbeer.net/dbui/%{name}-%{version}.tar.gz
# Source0-md5:	962828bfc9bdb64697111624090bcfef
URL:		http://spyder.virtualbeer.net/dbui/
# BuildRequires:	postgresql-devel
BuildRequires:	gtk+-devel
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's a GTK+ interface to MySQL/PostgreSQL databases. You might say a
database editor. It's still in its very early stages but you can fully
search, update, add, and delete any MySQL/PostgreSQL database.

%description -l pl.UTF-8
To jest interfejs GTK+ do baz danych MySQL/PostgreSQL. Można go nazwać
edytorem baz danych. Nadal jest we wstępnym stadium rozwoju, ale można
już przeszukiwać, uaktualniać, dodawać i usuwać z baz
MySQL/PostgreSQL.

%package mysql
Summary:	dbui linked with MySQL
Summary(pl.UTF-8):   dbui skonsolidowane z MySQL
Group:		Applications/Databases/Interfaces
Requires:	%{name} = %{version}-%{release}

%description mysql
dbui linked with MySQL.

%description mysql -l pl.UTF-8
dbui skonsolidowane z MySQL.

%package postgresql
Summary:	dbui linked with PostgreSQL
Summary(pl.UTF-8):   dbui skonsolidowane z PostgreSQL
Group:		Applications/Databases/Interfaces
Requires:	%{name} = %{version}-%{release}

%description postgresql
dbui linked with PostgreSQL.

%description postgresql -l pl.UTF-8
dbui skonsolidowane z PostgreSQL.

%prep
%setup  -q

%build
%{__make} -f Makefile.mysql
mv -f dbui dbui.mysql

#due to incompatibility with latest postgres libraries it doesn't compile
#correctly
# %{__make} -f Makefile.postgres
# mv -f dbui dbui.postgresql

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install dbui.mysql $RPM_BUILD_ROOT%{_bindir}
# install dbui.postgresql $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dbui.mysql

# %files postgresql
# %defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/dbui.postgresql
