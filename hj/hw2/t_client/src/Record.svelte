<script lang="ts">
    import { onMount } from 'svelte';
    import * as d3 from 'd3';

    let x = 125;
    let y = 125;

    let status : string = "";

    onMount(() => {
        let svg = d3.select("#record-svg")
                          .append('g')
                          .attr("transform", "translate(" + x + "," + y + ")");

        let data = {win: 9, lose: 20, draw:30}

        let text : string = (Math.round((data.win * 100) / (data.lose + data.draw))).toString() + "%"
        let color = d3.scaleOrdinal()
                      .domain(data)
                      .range(["#8ec0fa", "#ff6f69", "#81C784"]);

        // Compute the position of each group on the pie:
        let pie = d3.pie()
                    .value(function(d) {return d.value; })
        let data_ready = pie(d3.entries(data))

        svg.selectAll('path')
           .data(data_ready)
           .enter()
           .append('path')
           .attr('d', d3.arc()
                .innerRadius(80)
                .outerRadius(110)
            )
           .attr('fill', function(d){ return(color(d.data.key)) });

        svg.append("text")
           .text(text)
           .attr("x", -15);

        // status

        status = data.win.toString() + "W " + data.draw.toString() + "D " + data.draw.toString() + "L"
    });




</script>



<div id="record-view">
    <h3>{status}</h3>
    <svg id="record-svg"></svg>
</div>


<style>
    #record-view {
        margin-left: 25px;
        margin-right: 25px;
        display: block;
    }

    #record-svg {
        width: 250px;
        height: 250px;

    }

    h3 {
        color: #03254c;
		font-size: 1.5em;
        font-weight: 200;
        margin: 20px;
        margin-left: 25px;
        margin-top:14px;
        margin-bottom:9px;
        width: 200px;
    }

</style>