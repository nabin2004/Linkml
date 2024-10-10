
# Class: Person



URI: [personinfo:Person](https://w3id.org/linkml/examples/personinfo/Person)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Container]++-%20persons%200..*>[Person&#124;id:string;full_name:string;aliases:string%20*;phone:string%20%3F;age:integer%20%3F],[Container])](https://yuml.me/diagram/nofunky;dir:TB/class/[Container]++-%20persons%200..*>[Person&#124;id:string;full_name:string;aliases:string%20*;phone:string%20%3F;age:integer%20%3F],[Container])

## Identifier prefixes

 * ORCID

## Referenced by Class

 *  **None** *[➞persons](container__persons.md)*  <sub>0..\*</sub>  **[Person](Person.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [full_name](full_name.md)  <sub>1..1</sub>
     * Description: name of the person
     * Range: [String](types/String.md)
 * [aliases](aliases.md)  <sub>0..\*</sub>
     * Description: other names for the person
     * Range: [String](types/String.md)
 * [phone](phone.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [age](age.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | schema:Person |