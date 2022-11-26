<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Played On : {{ date }} Game Score: {{game.game_score}} </h1>
                <form @submit.prevent="submitForm2">
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Finish Game</button>
                        </div>
                    </div>
                </form>
            </div>
                <!-- For each unique player, generate a separate blcok for each word and score.
                    If that player is equal to the max value of any score, colour the background green !-->
                <p v-for="(g, index) in game.player_array" :key="index"> 
                    <div class="column is-12"> 
                        <p v-if="game.test[g.id]==maxVal">
                            <div class="box" v-bind:style="{ 'box-shadow' : '0 0.5em 1em -0.125em rgb(66 184 131 / 80%), 0 0px 0 1px rgb(10 10 10 / 2%)' }"> 
                                Player : {{ g.name }} ({{ game.test[g.id] }}) 
                                <p v-for="value in game.data">
                                    <p v-if="value.player_name==g.name">
                                        {{value.word}} ({{value.score}})
                                    </p>
                                </p>
                            </div>
                        </p>
                        <p v-else>
                            <div class="box">Player : {{ g.name }} ({{ game.test[g.id] }})
                                <p v-for="value in game.data">
                                    <p v-if="value.player_name==g.name">
                                        {{value.word}} ({{value.score}})
                                    </p>
                                </p>
                            </div>
                        </p>
                    </div>
                </p>
                <!-- Submit form for adding a new word and score !-->
                <div class="column is-12">
                    <form @submit.prevent="submitForm">
                        <div class="field">
                            <label>Player</label>
                            <div class="control">
                                <div class="select">
                                    <select v-model="player">
                                        <option v-for="item, in game.player_array" :value="item.id">{{item.name}}</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="field">
                            <label>Word</label>
                            <div class="control">
                                <input type="text" class="input" v-model="word">
                            </div>
                        </div>
                        <div class="field">
                            <label>Score</label>
                            <div class="control">
                                <input type="text" class="input" v-model="score">
                            </div>
                        </div>
                        <div class="field">
                            <div class="control">
                                <button class="button is-dark">Submit</button>
                            </div>
                        </div>
                    </form>
                </div>  
            </div>
        </div>
</template>

<script>
    import axios from 'axios'
    export default { 
        name: 'Game',
        data() { 
            return { 
                game: {},
                date: '',
                players: '',
                playerIDs: '',
                maxVal: '',
                newDate: '',
                id: '',
                last: '',
                lastTurn: '',
                turn: '',
                game_id: '',
                player: '',
                word: '',
                score: '',
                playerScores: '',
                winningScore: '',
                winningPlayer: '',
            }
        },
        // This is to get the data from Django
        mounted() { 
            this.getGame() 
        },
        methods: { 
            async getGame() { 
                this.$store.commit('setIsLoading', true)
                const GameID = this.$route.params.id

                axios
                    .get(`/api/v1/games/${GameID}/`)
                    .then(response => { 
                        this.game = response.data

                        this.date = this.game.date.substring(0, this.game.date.indexOf("T"));

                        // Get unique players, and map their info to an array
                        // This is used for the player form
                        this.players = [...new Set(this.game.data.map(x => x.player))];
                        if (this.players.length == 0) { this.playerIDs = this.game.player_array} else { this.playerIDs = this.players.map(player => this.game.data.find(x => x.player === player));}
                        
                        this.last = this.game.data[this.game.data.length-1];
                        try { (this.lastTurn = this.last.turn); } catch(err) { this.turn = 1 }

                        let arr = Object.values(this.game.test);
                        let max = Math.max(...arr);
                        this.maxVal = max
                        this.id = this.game.id

                        // Get the winner
                        this.playerScores = this.game.data.reduce((ac,a) => {
                            let ind = ac.findIndex(x => x.player === a.player);
                            ind === -1 ? ac.push(a) : ac[ind].score += a.score;
                            return ac;
                            },[])

                        this.winningScore = Math.max(...this.game.data.map(e => e.score));
                        this.winningPlayer = this.game.data.find(game => game.score === this.winningScore).player;

                    })
                    .catch(error => { 
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },

            async submitForm() { 
                this.$store.commit('setIsLoading', true)
                const lead = { 
                    game: this.id,
                    turn: this.lastTurn+1,
                    player: this.player,
                    word: this.word,
                    score: this.score,
                }
                await axios
                    .post('/api/v1/words/', lead)
                    .then(response => { 
                        console.log(response)
                        this.$router.push( this.$router.go() )
                    })
                    .catch(error => { 
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            },

            async submitForm2() { 
                const data2 = { 
                    winner: this.winningPlayer
                }

                await axios
                    .patch(`/api/v1/games/${this.id}/`, data2)
                    .then(response => { 
                        this.$router.push( this.$router.go() )
                    })
            }
        }
    }
</script>