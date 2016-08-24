$(document).ready(function () {

  Em.I18n.translations = jQuery.extend(Em.I18n.translations, {

    'app.name': 'Ops-Centor',
    'app.name.subtitle': '{0} Ops-Centor',
    'app.name.subtitle.experimental': 'Experimental',

    'app.versionMismatchAlert.title': 'Server / Web Client Version Mismatch',
    'app.versionMismatchAlert.body': 'Server and Web Client versions do not match:<br> ' +
    '<br>Server: <strong>{0}</strong>' +
    '<br>Web Client: <strong>{1}</strong><br>' +
    '<br>This typically happens after upgrading due to Web Client code cached in the browser.' +
    '<br>Perform a hard browser cache refresh, typically \'Ctrl+Shift+R\' (\'Cmd+Shift+R\' on OS X), to see if this message disappears.' +
    '<br>If you keep seeing this message, clear the browser cache completely and hit this URL again.' +
    '<br>You must resolve this error in order to continue.',
    'app.signout': 'Sign out',
    'app.settings': 'Settings',
    'app.manageAmbari': 'Manage',
    'app.aboutAmbari': 'About',

    'app.aboutAmbari.getInvolved': 'Built on Apache Ambari Platform!',
    'app.aboutAmbari.version': 'Version',
    'app.aboutAmbari.licensed': 'Copyright 2016 Yaana Technologies. All rights reserved.',

    'common.persist.error': 'Error in persisting web client state at server:',
    'common.update.error': 'Error in retrieving web client state from server',

    'popup.dependent.configs.title': 'Based on your configuration changes, We are recommending the following dependent configuration changes. <br/> We will update all checked configuration changes to the <b>Recommended Value</b>. Uncheck any configuration to retain the <b>Current Value</b>.',

    'popup.jdkValidation.body': 'The {0} Stack requires JDK {1} but Server is configured for JDK {2}. This could result in error or problems with running your cluster.',

    'login.error.bad.connection': 'Unable to connect to Server. Confirm Server is running and you can reach Server from this machine.',

    'topnav.logo.href': '/#/main/dashboard',
    'topnav.help.href': 'https://cwiki.apache.org/confluence/display/AMBARI/Ambari',

    'admin.stackVersions.manageVersions.popup.body': 'You are about to leave the <b>Cluster Management</b> interface' +
    ' and go to the <b>Administration</b> interface. You can return to cluster management by using the' +
    ' “Go to Dashboard” link in the Administration > Clusters section.',

  });
});