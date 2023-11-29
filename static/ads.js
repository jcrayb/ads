function insert_ad(div_id){
    fetch("/fetch/generate", {
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
    fetch(`/fetch/ad/${ad_id}?h=${height}&w=${width}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data =>{
        console.log(data)
        document.getElementById(div_id).innerHTML = `
        <a class="text-decoration-none text-black"
        href="/fetch/redirect/${ad_id}?website=${window.location.host}">`+data['code']+"</a>"
    }
    ).catch(error=>{
        console.error(error)
    })
};