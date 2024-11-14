#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Pokemon_Participante {
    string apelido;
    int poder_individual;
    int indice_original;
};

bool comparador(const Pokemon_Participante& a, const Pokemon_Participante& b) {
    if (a.poder_individual == b.poder_individual) {
        if (a.apelido == b.apelido) {
            return a.indice_original < b.indice_original;
        }
        return a.apelido > b.apelido;
    }
    return a.poder_individual > b.poder_individual;
}

int main() {
    int total_pokemons;
    cin >> total_pokemons;

    vector<Pokemon_Participante> lista_pokemons(total_pokemons);
    for (int i = 0; i < total_pokemons; ++i) {
        cin >> lista_pokemons[i].apelido >> lista_pokemons[i].poder_individual;
        lista_pokemons[i].indice_original = i;
    }

    vector<string> registro_batalhas;

    while (lista_pokemons.size() > 1) {
        sort(lista_pokemons.begin(), lista_pokemons.end(), comparador);

        Pokemon_Participante primeiro_pokemon = lista_pokemons[0];
        Pokemon_Participante segundo_pokemon = lista_pokemons[1];

        string batalha = primeiro_pokemon.apelido + " (" + to_string(primeiro_pokemon.poder_individual) + ") x (" +
                         to_string(segundo_pokemon.poder_individual) + ") " + segundo_pokemon.apelido + " : ";

        if (primeiro_pokemon.poder_individual == segundo_pokemon.poder_individual) {
            registro_batalhas.push_back(batalha + "empate");
            lista_pokemons.erase(lista_pokemons.begin());
            lista_pokemons.erase(lista_pokemons.begin());
        } else if (primeiro_pokemon.poder_individual > segundo_pokemon.poder_individual) {
            registro_batalhas.push_back(batalha + primeiro_pokemon.apelido + " venceu");
            lista_pokemons[0].poder_individual -= segundo_pokemon.poder_individual;
            lista_pokemons.erase(lista_pokemons.begin() + 1);
        } else {
            registro_batalhas.push_back(batalha + segundo_pokemon.apelido + " venceu");
            lista_pokemons[1].poder_individual -= primeiro_pokemon.poder_individual;
            lista_pokemons.erase(lista_pokemons.begin());
        }
    }

    if (lista_pokemons.empty()) {
        registro_batalhas.push_back("nenhum vencedor");
    } else {
        Pokemon_Participante campeao = lista_pokemons[0];
        registro_batalhas.push_back(campeao.apelido + " venceu com " + to_string(campeao.poder_individual));
    }

    for (const auto& batalha : registro_batalhas) {
        cout << batalha << endl;
    }

    return 0;
}
