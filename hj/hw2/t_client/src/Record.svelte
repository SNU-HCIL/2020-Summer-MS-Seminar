<script lang="ts">
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { idStore } from "./stores"

    let x = 100;
    let y = 100;

    let status : string = "";

    let svg;
    let pies;
    let text;

    let win : number = 0;
    let lose : number = 0;
    let draw : number = 0;

    let colors = ["#8ec0fa", "#ff6f69", "#81C784", "#888888"];

    let id;

    function updateRecord() {
        let spare : number;
        if((win + lose + draw == 0)) spare = 1;
        else                         spare = 0;

        let data = {win: win, lose: lose, draw: draw, spare: spare};
        let statusStr : string = (Math.round((data.win * 100) / (data.lose + data.draw + data.win + data.spare))).toString() + "%";

        let pie = d3.pie()
                    .value(function(d) {return d.value; })
        let data_ready = pie(d3.entries(data))

        let color = d3.scaleOrdinal()
                      .domain(data)
                      .range(colors);

        pies.data(data_ready)
            .join(
                enter => enter.append('path')
                              .attr('d', d3.arc()
                                    .innerRadius(75)
                                    .outerRadius(100)
                               )
                                .attr('fill', function(d){ return(color(d.data.key)) }),
                update => update
                                .attr('d', d3.arc()
                                    .innerRadius(75)
                                    .outerRadius(100)
                                ),
            );

                  

        text.text(statusStr);

        // status
        status = data.win.toString() + "W " + data.draw.toString() + "D " + data.lose.toString() + "L";

    }

    onMount(() => {

        svg = d3.select("#record-svg")
                .append('g')
                .attr("transform", "translate(" + x + "," + y + ")");

        let data = {win: win, lose: lose, draw: draw, spare:1}

        let statusStr : string = (Math.round((data.win * 100) / (data.lose + data.draw + data.win + data.spare))).toString() + "%"
        let color = d3.scaleOrdinal()
                      .domain(data)
                      .range(colors);

        // Compute the position of each group on the pie:
        let pie = d3.pie()
                    .value(function(d) {return d.value; })
        let data_ready = pie(d3.entries(data))

        pies = svg.selectAll('path')
                  .data(data_ready)
                  .enter()
                  .append('path')
                  .attr('d', d3.arc()
                          .innerRadius(75)
                          .outerRadius(100)
                      )
                  .attr('fill', function(d){ return(color(d.data.key)) });

        text = svg.append("text")
                  .text(statusStr)
                  .attr("x", -15);

        // status
        status = data.win.toString() + "W " + data.draw.toString() + "D " + data.lose.toString() + "L";


        // subscribe

        idStore.subscribe( v => { id = v; } )

    });




</script>



<div id="record-view">
    <h3>{status}</h3>
    <svg id="record-svg"></svg>
    <h4>signed in as {id}</h4>
    <!--For test : buttons-->
    <button on:click={() => {
        win += 1;
        updateRecord();
    }}>W</button>
    <button on:click={() => {
        draw += 1;
        updateRecord();
    }}>D</button>
    <button on:click={() => {
        lose += 1;
        updateRecord();
    }}>L</button>

</div>


<style>
    #record-view {
        margin-left: 25px;
        margin-right: 25px;
        display: block;
    }

    #record-svg {
        width: 200px;
        height: 200px;

    }

    h3 {
        color: #03254c;
		font-size: 1.5em;
        font-weight: 200;
        margin: 20px;
        margin-left: 25px;
        margin-top: 23px;
        margin-bottom: 15px;
        width: 200px;
    }

    h4 {
        color: #03254c;
		font-size: 1em;
        font-weight: 200;
        margin: 20px;
        margin-left: 25px;
        margin-top:14px;
        margin-bottom:9px;
        width: 200px;
    }

</style>