<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{player.name}}</h1>
                <p>{{player.email}}</p><br>
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Games Played</th>
                            <th>Total Score</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{{ gamesPlayed }}</td>
                            <td>{{ totalScore }}</td>
                        </tr>
                    </tbody>
                </table>
                <div v-if="loaded"> 
                <h3 class="title">Win Ratio ({{ (wins/gamesPlayed).toFixed(2)*100 }}%)</h3>
                <PieChart :chart-data="chartData3"/><br>

                <h3 class="title">Word Cloud</h3>
                    <WordCloud 
                    :data="wordDict"
                    nameKey="name"
                    valueKey="value"
                    :color="myColors"
                    :showTooltip="true"
                    :wordClick="wordClickHandler">
                </WordCloud>
                <h3 class="title">Top 5 Words</h3>
                <BarChart :chart-data="chartData" /><br>

                <h3 class="title">Word Length</h3>
                <BarChart :chart-data="chartData2" />
                x = length of word,    y = count
                </div>
            </div>
        </div>
    </div>
</template>

<script >
    import axios from 'axios'
    import WordCloud from './Cloud'
    import BarChart from './BarChart'
    import PieChart from './PieChart'

    export default { 
        name: 'Player',
        components: {
            WordCloud, BarChart, PieChart
        },
        data() { 
            return { 
                // Colours for the wordcloud
                myColors: ['#1c1e21', '#373b41', '#525861', '#525861'],
                player: [],
                words: '',
                wordDict: '',
                loaded: false,
                gamesPlayed: '',
                totalScore: '',

                wordFreq: '',
                freqResult: '',  
                top5: '',

                wordLength: '',
                wordLengthCount: '',

                wins: '',

                chartData: {
                labels: [  ],
                datasets: [ { data: [] , backgroundColor: ['#1c1e21', '#424448', '#6D6F73', '#9A9DA0', '#CACDD1'] } ],
                },

                chartData2: {
                labels: [  ],
                datasets: [ { data: [] , backgroundColor: ['#1c1e21', '#424448', '#6D6F73', '#9A9DA0', '#CACDD1'] } ],
                },

                chartData3: {
                labels: [  "Games Won", "Games Lost"],
                datasets: [ { data: [] , backgroundColor: [ '#6D6F73', '#424448' ] } ],
                },    
            }
        },
        mounted() { 
            this.getPlayer()
            
        },
        methods: { 
            async getPlayer() { 
                this.$store.commit('setIsLoading', true)
                const PlayerID = this.$route.params.id
                axios
                    .get(`/api/v1/user/${PlayerID}/`)
                    .then(response => { 
                        this.player = response.data

                        this.words = [...(this.player.test.map(x => x.word))];
                        this.wordDict = Array.from(new Set(this.words)).map(a => ({name:a, value: this.words.filter(f => f === a).length}));

                        this.loaded = true
                        this.gamesPlayed = [...new Set(this.player.test.map(item => item.game))].length
                        this.totalScore = this.player.test.reduce((acc, item) =>acc + item.score, 0)

                        // Player word frequency
                        this.wordFreq = this.words.reduce(
                            (acc, curr) => acc.set(curr, (acc.get(curr) || 0) + 1),
                            new Map()
                            );
                        this.freqResult = [...this.wordFreq.entries()].reduce((acc, [key, value]) => {
                        if (value >= 2.0) acc[key] = value;
                        return acc;
                        }, {});
                        this.top5 = Object
                        .entries(this.freqResult) // create Array of Arrays with [key, value]
                        .sort(([, a],[, b]) => b-a) // sort by value, descending (b-a)
                        .slice(0,5) // return only the first 3 elements of the intermediate result
                        
                        for (const x of this.top5) { this.chartData.labels.push(x[0]); }
                        for (const x of this.top5) { this.chartData.datasets[0].data.push(x[1]); }

                        // Player word length
                        this.wordLength = this.words.map(w => w.length);
                        var counts = {};
                        this.wordLength.forEach(function (x) { counts[x] = (counts[x] || 0) + 1; });
                        this.wordLengthCount = counts
                        
                        this.chartData2.datasets[0].data = Object.keys(counts).map(function(key){
                            return counts[key];
                        });

                        this.chartData2.labels = Object.keys(counts).map(function(key){
                            return key;
                        });
                        
                        // Player total games
                        this.wins = this.player.test.filter(function(v) {
                            return this[v.game]?
                                !Object.assign(this[v.game], v):
                                (this[v.game] = v);
                            }, {});

                        this.wins = this.wins.filter(x => x.winner === (this.player.id).toString()).length;

                        this.chartData3.datasets[0].data = [this.wins, (this.gamesPlayed-this.wins)]
                    })
                    .catch(error => { 
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
            async wordClickHandler(name, value, vm) {
                console.log('wordClickHandler', name, value, vm);
            },
        },
    }
</script>


