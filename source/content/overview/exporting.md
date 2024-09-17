# Exporting

## Exporting to `ecospold` 1

Brightway can export inventory datasets conforming to the latest version of the ecospold version 1 [schema documentation](https://github.com/brightway-lca/pyecospold/tree/main/pyecospold/schemas/v1).

`ecospold` 1 documents describe processes who produce and consume products. The {py:obj}`bw2io.export.ecospold1.Ecospold1Exporter` operates on individual nodes, and it is up to you to pass nodes of the correct type to the exporter.

The `ecospold` 1 format uses a lot of fields which practitioners don't normally populate. When importing `ecospold` 1, we store most of this information as "tags". The main exception are comment fields; the `Ecospold1Exporter` requires that the `comments` field be a dictionary, not a string. This is because we need to break comments up into several fields in the XML export. No keys in this dictionary are required, and the fields used are listed below.

### Nodes

The following node attributes are *required* for a valid `ecospold` 1 export:

| Brightway node attribute | `ecospold` 1 XPath |
| --- | --- |
| name | ecoSpold/dataset/metaInformation/processInformation/referenceFunction/@name |
| unit | ecoSpold/dataset/metaInformation/processInformation/referenceFunction/@unit |

The following *optional* attributes can be included, and are considered useful by most `ecospold` importers.

In `ecoSpold/dataset/metaInformation/processInformation/referenceFunction`:

| Brightway data schema | Default value | `ecospold` 1 XPath |
| --- | --- | --- |
| comments["includedProcesses"] | empty string | @includedProcesses |
| tags["ecoSpold01category"] | empty string| @category |
| tags["ecoSpold01datasetRelatesToProduct"] | `true` | @datasetRelatesToProduct |
| tags["ecoSpold01infrastructureIncluded"] | `false` | @infrastructureIncluded |
| tags["ecoSpold01infrastructureProcess"] | `false` | @infrastructureProcess |
| tags["ecoSpold01localCategory"] | tags["ecoSpold01category"] | @localCategory |
| tags["ecoSpold01localName"] | name | @localName |
| tags["ecoSpold01localSubCategory"] | tags["ecoSpold01subCategory"] | @localSubCategory |
| tags["ecoSpold01subCategory"] | empty string| @subCategory |

In `ecoSpold/dataset/metaInformation/processInformation/geography`:

| Brightway data schema | Default value | `ecospold` 1 XPath |
| --- | --- | --- |
| comments["location"] | empty string | @text |
| location | "GLO" | @location |

In `ecoSpold/dataset/metaInformation/processInformation/technology`:

| Brightway data schema | Default value | `ecospold` 1 XPath |
| --- | --- | --- |
| comments["technology"] | empty string | @text |

In `ecoSpold/dataset/metaInformation/processInformation/timePeriod`:

| Brightway data schema | Default value | `ecospold` 1 XPath |
| --- | --- | --- |
| comments["timePeriod"] | empty string | @text |
| tags["dataValidForEntirePeriod"] | `true` | @dataValidForEntirePeriod |
| tags["ecoSpold01endDate"] | "1970-01-01" | endData/text() |
| tags["ecoSpold01startDate"] | "1970-01-01" | startData/text() |

In `ecoSpold/dataset/metaInformation/processInformation/timePeriod`:

| Brightway data schema | Default value | `ecospold` 1 XPath |
| --- | --- | --- |
| comments["timePeriod"] | empty string | @text |
| tags["dataValidForEntirePeriod"] | `true` | @dataValidForEntirePeriod |
| tags["ecoSpold01endDate"] | "1970-01-01" | endData/text() |
| tags["ecoSpold01startDate"] | "1970-01-01" | startData/text() |

In `ecoSpold/dataset/metaInformation/processInformation/dataSetInformation`:

| Brightway data schema | Default value | `ecospold` 1 XPath |
| --- | --- | --- |
| tags["ecoSpold01impactAssessmentResult"] | `false` | @impactAssessmentResult |
| tags["ecoSpold01internalVersion"] | "0.0" | @internalVersion |
| tags["ecoSpold01languageCode"] | "en" | @languageCode |
| tags["ecoSpold01localLanguageCode"] | "de" | @localLanguageCode |
| tags["ecoSpold01timestamp"] | datetime.now().isoformat() | @timestamp |
| tags["ecoSpold01type"] | "1" | @type |
| tags["ecoSpold01version"] | "0.0" | @version |

In `ecoSpold/dataset/metaInformation/modellingAndValidation/representativeness`:

| Brightway data schema | Default value | `ecospold` 1 XPath |
| --- | --- | --- |
| comments["extrapolations"] | "unknown" | @extrapolations |
| comments["productionVolume"] | "unknown" | @productionVolume |
| comments["sampling"] | "unknown" | @samplingProcedure |
| comments["uncertaintyAdjustments"] | "unknown" | @uncertaintyAdjustments |

#### References

If provided, `node["references"]` should be a list attached to nodes. Each element in the list is a dictionary. This dictionary does not have any required attributes, but the following can be provided in each "reference" dictionary:

In `ecoSpold/dataset/metaInformation/modellingAndValidation/source`:

| Brightway data schema | Default value | `ecospold` 1 XPath |
| --- | --- | --- |
| anthology | skipped if missing | @titleOfAnthology |
| authors[0] | empty string | @firstAuthor |
| authors[1:] | empty string | @additionalAuthors |
| editors | skipped if missing | @nameOfEditors |
| identifier | node numerical index | @number |
| issue | skipped if missing | @issueNo |
| journal | skipped if missing | @journal |
| pages | skipped if missing | @pageNumbers |
| place_of_publication | skipped if missing | @placeOfPublications |
| publisher | skipped if missing | @publisher |
| text | skipped if missing | @text |
| title | skipped if missing | @title |
| type | "Undefined (default)" | @sourceType |
| volume | skipped if missing | @volumeNo |
| year | skipped if missing | @year |

The `reference_element["authors"]` field, if given, should be a list of strings.

The `reference_element["type"]` field, if given, should be one of:

* "Undefined (default)"
* "Article"
* "Chapters in anthology"
* "Seperate publication"
* "Measurement on site"
* "Oral communication"
* "Personal written communication"
* "Questionnaries"

### Edges

The following edge attributes are *required* for each `exchange` element in `ecoSpold/dataset/flowData` for a valid `ecospold` 1 export:

| Brightway edge attribute | `ecospold` 1 XPath |
| --- | --- |
| unit | ecoSpold/dataset/flowData/exchange/@unit |
| name | ecoSpold/dataset/flowData/exchange/@name |
| amount | ecoSpold/dataset/flowData/exchange/@meanValue |

The edge "type" will set the `ecospold` 1 `inputGroup` or `outputGroup` value using the following mapping:

| Brightway edge type | `ecospold` 1 `inputGroup` | `ecospold` 1 `outputGroup` |
| --- | --- |
| technosphere | "5" | |
| production | | "0" |
| substitution | | "1" |
| biosphere[^1] | "5" | "4" |

[^1]: The function will choose between `inputGroup` and `outputGroup` based on the `categories` attribute.

If uncertainty information is given, this uncertainty information should follow the `stats_arrays` data schema. All uncertainty fields will be translated to `ecospold` 1 equivalents.

The following *optional* attributes can be included, and are considered useful by most `ecospold` importers.

| Brightway data schema | Default value | `ecospold` 1 XPath |
| --- | --- | --- |
| caetgories[0] | empty string | @category |
| caetgories[1] | empty string | @subCategory |
| CAS number | skipped if empty | @CASNumber |
| chemical formula | skipped if empty | @formula |
| comment | skipped if empty | @generalComment |
| infrastructureProcess | `false` | @infrastructureProcess |
| location | skipped if empty | @location |
| pages | skipped if empty | @pageNumbers |
| source_reference | skipped if empty | @referenceToSource |
| uncertainty type | skipped if empty[^2] | @uncertaintyType |

[^2]: Translated from `stats_arrays` integer ids to the `ecospold` 1 schema
