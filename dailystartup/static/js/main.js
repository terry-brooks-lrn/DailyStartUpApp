(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });


    // Sidebar Toggler
    $('.sidebar-toggler').click(function () {
        $('.sidebar, .content').toggleClass("open");
        return false;
    });


})(jQuery);

function CatchyPhrase(type) {
    if (type == 'resolve') {
        const completionText = ['Item Has Been Resolved - Good Work Team!', 'Another One Bites The Dust', 'Done and dusted, Item Busted.', 'Get your tasks done, like a boss!', 'Nothing But Net']
        return completionText[Math.floor(Math.random() * completionText.length)]

    } else if (type == 'monitor') {
        const completionText = ['And Now Our Watch Begins', 'We\'ve got our eyes on you', 'Almost Little One.']
        return completionText[Math.floor(Math.random() * completionText.length)]

    }
};

// Event Listensers to open and close the `add item modals`

// Countdown for Reset Pass
function onSignIn(googleUser) {
    var id_token = googleUser.getAuthResponse().id_token;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://yourbackend.example.com/tokensignin');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        console.log('Signed in as: ' + xhr.responseText);
};
xhr.send('idtoken=' + id_token);
  }