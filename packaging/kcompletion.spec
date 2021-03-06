# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kcompletion

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 2 addon for completion
Version:    5.3.0
Release:    2
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kcompletion.yaml
Source101:  kcompletion-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  kconfig-devel
BuildRequires:  kconfig-gui
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  gettext-devel

%description
KCompletion provides widgets with advanced completion support as well as a
lower-level completion class which can be used with your own widgets.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kconfig-devel
Requires:   kconfig-gui
Requires:   kwidgetsaddons-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
%find_lang kcompletion5_qt --with-qt --all-name || :
# << install pre

# >> install post
# << install post

%files -f kcompletion5_qt.lang
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5Completion.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/kcompletion_version.h
%{_kf5_includedir}/KCompletion
%{_kf5_libdir}/libKF5Completion.so
%{_kf5_cmakedir}/KF5Completion
%{_kf5_mkspecsdir}/qt_KCompletion.pri
# >> files devel
# << files devel
