$(document).ready(function() {
    $(".header").height($(window).height());

});

$(window).on('load', function(){
    filter_sentences();
    change_label_css();
    
} );

function filter_sentences(){
    // This function set the initial check boxes checked
    // If a sentence has no tag related to checked checkbox
    // that sentence will be blurred

    //sanity check
    //console.log("In filter function");
    $('#DES').prop("checked", true);
    $('#CW').prop("checked", true);
    $('#Org').prop("checked", true);
    $('#QT').prop("checked", true);
    $('#RES').prop("checked", true);
    $('#Topic').prop("checked", true);

    var chkIDs = checkArray();
    let a = new Set(chkIDs);

    var list_items, classes, matches;

    list_items = document.querySelectorAll(".sent");

    for (item of list_items){
        //console.log(item.classList)
        classes = item.classList;
        let b = new Set(classes)
        matches = new Set([...a].filter(x => b.has(x))); 
        //console.log(matches);
        if (matches.size === 0){
            item.classList.add("special-card");
        }
        else if (matches.size >= 1){
            item.classList.remove("special-card");
        }
    }
}

function checkArray(){
    
    $checkbox = $('.filter');

    var chkArray = [];
    chkArray = $.map($checkbox, function(el){
        if(el.checked){return el.id}
    });
    //console.log(chkArray);
    return chkArray;
}

const labelClassMap = {
    "OT" : "badge badge-warning",
    "RES" : "badge badge-success",
    "DES" : "badge badge-light",
    "CW" : "badge badge-info",
    "Org" : "badge badge-info",
    "QT" : "badge badge-info",
    "Topic" : "badge badge-primary",
    "URL" : "badge badge-secondary",
    "Code" : "badge badge-dark"
}

function change_label_css(){
    // This function captuer all elements with ID=badge and store in labels array
    // Then we iterate through each element (in this case label) 
    // and add classes according to map
    
    //Sanity check
    // console.log("Changing CSS classes");
    
    var labels, j;
    labels = document.querySelectorAll(".badge");
    // console.log(labels)
    
    for (label of labels){
        label.classList.add(...labelClassMap[label.textContent].split(" "));
    }
}

$(".filter").change(function(){
    var chkIDs = checkArray();
    let a = new Set(chkIDs);

    var list_items, classes, matches;

    list_items = document.querySelectorAll(".sent");

    for (item of list_items){
        //console.log(item.classList)
        classes = item.classList;
        let b = new Set(classes)
        matches = new Set([...a].filter(x => b.has(x))); 
        //console.log(matches);
        if (matches.size === 0){
            item.classList.add("special-card");
        }
        else if (matches.size >= 1){
            item.classList.remove("special-card");
        }
    }
});

// check which topic words checked once the document is ready
$(".topic-check").change(function(){
    var chkTopicIDs = checkTopics();
        
    list_items = document.querySelectorAll(".sent");

    if (chkTopicIDs.length != 0){
        var pattern = new RegExp(chkTopicIDs.join("|"));

        for (item of list_items){
            var text = item.textContent;
            
            if (pattern.test(text)){
                item.classList.add("highlight");
            }
            else {
                item.classList.remove("highlight");
            }
        }
    }
    else if (chkTopicIDs.length == 0){
        console.log("None checked");
        for (item of list_items){
            item.classList.remove("highlight");
        }
    }
    
});

// check which topics are checked
function checkTopics(){
    
    $checkbox = $('.topic-check');

    var chkArray = [];
    chkArray = $.map($checkbox, function(el){
        if(el.checked){return el.id}
    });
    
    return chkArray;
}


