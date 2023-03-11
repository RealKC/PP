package org.example

class Birth(val year: Int, val month: Int, val day: Int) {
    override fun toString(): String {
        return "($day.$month.$year)"
    }
}

class Contact(val name: String, var phone: String, val birthDate: Birth) {
    fun print() {
        println("Name: $name, Mobile: $phone, Date: $birthDate")
    }
}

fun search(agenda: List<Contact>, nameOrPhoneNumber: String, isPhoneNumber: Boolean): Contact? {
    if (isPhoneNumber) {
        for (contact in agenda) {
            if (contact.phone == nameOrPhoneNumber) {
                return contact
            }
        }
    } else {
        for (contact in agenda) {
            if (contact.name == nameOrPhoneNumber) {
                return contact
            }
        }
    }

    return null
}

fun updatePhoneNumber(agenda: MutableList<Contact>, name: String, newPhoneNumber: String) {
    for (contact in agenda) {
        if (contact.name == name) {
            contact.phone = newPhoneNumber
            break
        }
    }
}

fun main(args: Array<String>) {
    val agenda = mutableListOf<Contact>()
    agenda.add(Contact("Mihai", "0744321987", Birth(1900, 11, 25)))
    agenda += Contact("George", "0761332100", Birth(2002, 3, 14))
    agenda += Contact("Liviu", "0231450211", Birth(1999, 7, 30))
    agenda += Contact("Popescu", "0211342787", Birth(1955, 5, 12))

    for (persoana in agenda) {
        persoana.print()
    }

    println("Agenda dupa eliminare contact [George]:")
    agenda.removeAt(1)

    for (persoana in agenda) {
        persoana.print()
    }

    agenda.remove(Contact("Liviu", "0231450211", Birth(1999, 7, 30)))
    println("Agenda dupa eliminare contact [Liviu]:")
    agenda.removeAt(1)

    for (persoana in agenda) {
        persoana.print()
    }

    println("Cautare dupa nume: 'Popescu'")
    search(agenda, "Popescu", false)!!.print()

    println("Cautare dupa numar de telefon: '0744321987'")
    search(agenda, "0744321987", true)!!.print()

    println("Cautare dupa persoane inexistenta: 'Matei'")
    val res = search(agenda, "Matei", false)
    if (res == null) {
        println("-> nu exista")
    } else {
        res.print()
    }

    println("Popescu si-a schimbat nr de tel: 0479994441")
    updatePhoneNumber(agenda, "Popescu", "0479994441")
    for (persoana in agenda) {
        persoana.print()
    }
}

