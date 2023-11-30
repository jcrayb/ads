function generate_ad_spots(){
    ad_spots = document.getElementsByClassName('ad');
    console.log(ad_spots)
    i = 0
    Array.from(ad_spots).forEach(element =>{
        element.id = "ad_spot_"+i;
        element.classList.add("bg-white", "border")
        insert_ad("ad_spot_"+i)
        i = i+1
    })
    //d-flex justify-content-center
}

function insert_ad(div_id){
    fetch("https://dev-ads.jcrayb.com/fetch/generate", {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data =>{
        ad_id = data['ad_id']
        get_ad_content(ad_id, div_id)
    }
    ).catch(error=>{
        console.error(error)
    });
}

function get_ad_content(ad_id, div_id){
    div = document.getElementById(div_id);
    height = div.clientHeight;
    width = div.clientWidth;
    console.log(height, width)
    fetch(`https://dev-ads.jcrayb.com/fetch/ad/${ad_id}?h=${height}&w=${width}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data =>{
        //content = `<a class="text-decoration-none text-black h-100 w-100" href="/fetch/redirect/${ad_id}?website=${window.location.host}">`
        content = data['code']
        console.log("()=> window.location.href ="+ `/fetch/redirect/${ad_id}?website=${window.location.host}`)
        redirect = new String(`/fetch/redirect/${ad_id}?website=${window.location.host}`)
        console.log(redirect)
        document.getElementById(div_id).setAttribute("onclick", `window.location.href = '${redirect}}`+"'")
        //content += "</a>"
        console.log(content)
        document.getElementById(div_id).innerHTML = content
    }
    ).catch(error=>{
        console.error(error)
    })
};