-- # Class: "Person" Description: ""
--     * Slot: id Description: 
--     * Slot: full_name Description: name of the person
--     * Slot: phone Description: 
--     * Slot: age Description: 
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Container" Description: ""
--     * Slot: id Description: 
-- # Class: "Person_aliases" Description: ""
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: aliases Description: other names for the person

CREATE TABLE "Container" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	full_name TEXT NOT NULL, 
	phone TEXT, 
	age INTEGER, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "Person_aliases" (
	"Person_id" TEXT, 
	aliases TEXT, 
	PRIMARY KEY ("Person_id", aliases), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id)
);