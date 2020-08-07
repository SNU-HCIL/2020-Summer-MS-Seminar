<script lang='ts'>
    import * as d3 from 'd3';
    import { onMount } from 'svelte';
    import { recordData } from '../store';
    import type { margin } from '../types';

    function translate(x, y) {
        return 'translate(' + x + ',' + y + ')'
    }

    let svgWidth: number = 550;
    let svgHeight: number = 550;
    let margin: margin = { top: 30, right: 10, bottom: 20, left: 40, mid: 10 };
    let width: number = svgWidth - margin.left - margin.right;
    let height: number = svgHeight - margin.top - margin.bottom;

    let el;
    let svg;


    let arc = d3.arc()
        .innerRadius(50)
        .outerRadius(200);

    
    onMount(() => {
        svg = d3.select(el)
        .append('svg')
        .attr('width', svgWidth)
        .attr('height', svgHeight)
        .append('g')
        .attr('transform', translate(margin.left, margin.top));
    })

    recordData.subscribe((value) => {

        let data: Array<number>;
        if(value) {

        }
        else {
            data = [] 
        }
        svg.selectAll('path')
        .data(data)
        .join('arc')
        .append('path')
        .attr('d', arc);
    })

</script>
<style>

</style>

<div bind:this={el}>

</div>