
const $cupcakeList = $("#cupcakes");

// Form inputs
const $flavor = $("#flavor");
const $size   = $("#size");
const $rating = $("#rating");
const $image  = $("#image");

getCupcakes();

// populate $cupcakeList with cupcakes present in database
async function getCupcakes() {
    const resp = await axios.get("/api/cupcakes");

    resp.data["cupcakes"].forEach(cupcake => addCupcake(cupcake));
}

$cupcakeList.click(handleDeleteCupcake);

$("form").on("submit", handleNewCupcakeForm);

async function handleNewCupcakeForm(evt) {
    evt.preventDefault();

    resp = await axios.post("/api/cupcakes", json={
        "flavor":   $flavor.val(),
        "size":     $size.val(),
        "rating":   $rating.val(),
        "image":    $image.val()  
    });

    cupcake = resp.data["cupcake"];

    addCupcake(cupcake);
}

async function handleDeleteCupcake(evt) {
    if (evt.target.tagName !== "BUTTON") return;
    
    const $cupcakeElement = $(evt.target).parent();

    await axios.delete(`/api/cupcakes/${$cupcakeElement.attr("id")}`);

    $cupcakeElement.remove();
}

function addCupcake(cupcake) {
    $cupcake = $("<div>").addClass("w-100 justify-content-center")
        .attr("id", cupcake["id"])
        .append([
            $("<h2>").addClass("display-5 text-center mt-3 mb-3 text-muted")
                .text(`${cupcake["flavor"]} Cupcake`),
            $("<h3>").addClass("display-7 text-center text-muted")
                .text(`Size: ${cupcake["size"]}`),
            $("<img>").addClass("rounded mx-auto d-block").attr({
                "src": cupcake["image"],
                "alt": `${cupcake["flavor"]} cupcake`
            }),
            $("<button>").addClass("btn btn-danger mt-3 mx-auto d-block")
                .text("Remove")
        ]);

    $cupcakeList.append($cupcake);
}