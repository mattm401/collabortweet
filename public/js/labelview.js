// Call when the document is ready


$( document ).ready(function() {
	console.log( "ready!" );

	loadDataElements();
});

var sendSelectedElement = function(elementId, selectedLabelId) {
	result = {
		element: elementId,
		selected: selectedLabelId,
	}

	$.post("/item", result, function(data) {
		console.log("Successfully sent selection...");
		loadDataElements();
	})
}

var loadDataElements = function() {

	console.log("loadDataElements() called.");
	$("#loadingDialog").modal('show');

	$.get("/item", function(json) {
		dataElement = json;

		if ( "empty" in dataElement ) {
			$("#loadingDialog").modal('hide');

			alert("You have no more elements in this task!");
			console.log("You have no more elements in this task!");

			// turn off the keypress function
			$(document).off("keypress");

			// Turn off the click handler
			$(this).off("click");

		} else {
			console.log("Acquired element...");

			$("#element-content-panel").html(dataElement.elementText);

var name = "";
$.getJSON('convertcsvarray.json', function (json) {
var array = [];
for (var key in json) {
    if (json.hasOwnProperty(key)) {
        var item = json[key];
        array.push({
            VideoId: item.VideoId,
            Title: item.Title,
            Author: item.Author,
            Published: item.Published

        });
        console.log(item);
    }
}
});
console.log(dataElement);

            $("#video").attr('src' , "https://www.youtube.com/embed/" );
			// turn off the keypress function
			$(document).off("keypress");

			$('.selected-label').each(function() {
				var labelIndex = $(this).attr('labelindex');
				var labelId = $(this).attr('labelid');

				console.log("Label Index: " + labelIndex);
				console.log("Label ID: " + labelId);

				// Set the click function for this label ID
				$(this).off("click").click(function() {
					sendSelectedElement(dataElement.elementId, labelId);
				});

				// Set the keypress for this label
				$(document).keypress(function(e) {
					if ( e.which-48 == labelIndex ) {
						sendSelectedElement(dataElement.elementId, labelId);
					}
				});
			});

			$("#loadingDialog").modal('hide');
			console.log("Loaded element...");
		}
	})

}