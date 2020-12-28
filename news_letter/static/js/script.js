window.onload = function() {
    // Get the Object by Tag
    var allObjects = document.getElementsByTagName("object");
    // Get the SVG document inside the Object tag
    var i;
    for (i = 0; i < allObjects.length; i++) {
        var objDoc = allObjects[i].contentDocument;
        var svg = objDoc.getElementsByTagName("svg")[0];
        var bbox = svg.getBBox();
        var viewBox = [bbox.x, bbox.y, bbox.width, bbox.height].join(" ");
        svg.setAttribute("viewBox", viewBox);
    }
};
