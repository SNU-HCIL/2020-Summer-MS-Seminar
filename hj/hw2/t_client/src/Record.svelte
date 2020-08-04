<script lang="ts">
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { winStore, loseStore, drawStore } from "./stores"

    let x = 125;
    let y = 125;

    let status : string = "";

    let svg;
    let pies;
    let text;

    let win : number = 0;
    let lose : number = 0;
    let draw : number = 0;

    let colors = ["#8ec0fa", "#ff6f69", "#81C784", "#888888"];

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
                                    .innerRadius(80)
                                    .outerRadius(110)
                               )
                                .attr('fill', function(d){ return(color(d.data.key)) }),
                update => update
                                .attr('d', d3.arc()
                                    .innerRadius(80)
                                    .outerRadius(110)
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

        let data = {win: 0, lose: 0, draw: 0, spare:1}

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
                          .innerRadius(80)
                          .outerRadius(110)
                      )
                  .attr('fill', function(d){ return(color(d.data.key)) });

        text = svg.append("text")
                  .text(statusStr)
                  .attr("x", -15);

        // status
        status = data.win.toString() + "W " + data.draw.toString() + "D " + data.lose.toString() + "L"


        // subscribe
        winStore.subscribe(v => {
            win = v;
            updateRecord();
        });

        drawStore.subscribe(v => {
            draw = v;
            updateRecord();
        });

        loseStore.subscribe(v => {
            lose = v;
            updateRecord();
        });

    });




</script>



<div id="record-view">
    <h3>{status}</h3>
    <svg id="record-svg"></svg>
    <!--For test : buttons-->
    <button on:click={() => {
        winStore.update(v => v + 1);
    }}>W</button>
    <button on:click={() => {
        drawStore.update(v => v + 1);
    }}>D</button>
    <button on:click={() => {
        loseStore.update(v => v + 1);
    }}>L</button>

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