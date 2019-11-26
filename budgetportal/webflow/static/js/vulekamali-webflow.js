(function() {

    // MapBox
    var accessToken = 'pk.eyJ1IjoiamJvdGhtYSIsImEiOiJjazF3aXZ3NnYwMjU4M29udWppMWp6enVxIn0.yGE8zxBnb4g6A1QadgGY7g'
    var provinceCode = {
        "Eastern Cape": "EC",
        "Free State": "FS",
        "Gauteng": "GT",
        "KwaZulu-Natal": "KZN",
        "Limpopo": "LIM",
        "Mpumalanga": "MP",
        "North West": "NW",
        "Northern Cape": "NC",
        "Western Cape": "WC"
    };
    var levelToCode = {
        "Local Municipality": "MN",
        "Metro Municipality": "MN",
        "District Municipality": "DC"
    };

    function formatCurrency(decimalString) {
        if (decimalString == null)
            return "";
        return "R " + Math.round(parseFloat(decimalString)).toLocaleString();
    }

    function createTileLayer() {
        return L.tileLayer('//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
            maxZoom: 18,
            subdomains: 'abc',
        });
    }

    function initPointMap(lat, lon) {
        var map = L.map("project-location-map-container")
            .setView([lat, lon], 13);
        createTileLayer().addTo(map);
        return map;
    }

    function initMuniMap(lat, lon) {
        var map = L.map("project-municipal-context-map-container")
            .setView([lat, lon], 7);
        createTileLayer().addTo(map);
        return map;
    }

    function addProvinceToMap(map, provinceName) {
        $.get("https://mapit.code4sa.org/area/MDB:" + provinceCode[provinceName] +
              "/feature.geojson?generation=2&simplify_tolerance=0.01")
            .done(function(response) {
                var layer = L.geoJSON(response, {
                    weight: 1,
                    "fillColor": "#66c2a5",
                    "fillOpacity": 0.3,
                })
                    .addTo(map)
                    .bindTooltip(function (layer) {
                        return layer.feature.properties.name + " Province";
                    }).addTo(map);

                map.fitBounds(layer.getBounds());
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
                console.error( jqXHR, textStatus, errorThrown );
            });
    }

    function addMuniToMap(map, provinceName, level, muniName) {
        var levelCode = levelToCode[level];
        $.get("https://mapit.code4sa.org/areas/MDB-levels:PR-" + provinceCode[provinceName] +
              "|" + levelCode + ".geojson?generation=2&simplify_tolerance=0.01")
            .done(function(response) {
                var munis = response.features.filter(function(feature) {
                    return feature.properties.name === muniName;
                });
                if (munis.length) {
                    var muni = munis[0]; // Assume no duplicate names in a province
                    var layer = L.geoJSON(muni, {
                        weight: 1,
                        "fillColor": "#66c2a5",
                        "fillOpacity": 0.3,
                    })
                        .addTo(map)
                        .bindTooltip(function (layer) {
                            return layer.feature.properties.name + " " + level;
                        }).addTo(map);
                } else {
                    console.info("Couldn't find muni " + muniName + " by name in province");
                }
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
                console.error( jqXHR, textStatus, errorThrown );
            });
    }


    if ($("body.provincial-infrastructure-project-detail-page").length) {
        var project = pageData.project;

        // Project definition
        $(".name-field").text(project.name);
        $(".project-number-field").text(project.project_number);
        $(".budget-programme-field").text(project.budget_programme);
        $(".nature-of-investment-field").text(project.nature_of_investment);

        // Administrative details
        $(".primary-funding-source-field").text(project.primary_funding_source);
        $(".funding-status-field").text(project.funding_status);
        $(".province-field").text(project.province);
        $(".department-field").text(project.department);

        // Location
        $("#local-municipality-field").text(project.local_municipality);
        $("#district-municipality-field").text(project.district_municipality);
        $(".coordinates-field").text(project.latitude + ", " + project.longitude);

        // Implementation
        $(".program-implementing-agent-field").text(project.program_implementing_agent);
        $(".principle-agent-field").text(project.principle_agent);
        $(".main-contractor-field").text(project.main_contractor);
        $(".other-service-providers-field").text(project.other_parties);

        // Dates
        $(".status-field").text(project.status);
        $(".start-date-field").text(project.start_date);
        $(".estimated-construction-start-date-field").text(project.estimated_construction_start_date);
        $(".estimated-completion-date-field").text(project.estimated_completion_date);
        $(".contracted-construction-end-date-field").text(project.contracted_construction_end_date);
        $(".estimated-construction-end-date-field").text(project.estimated_construction_end_date);

        // Budgets and spending
        $(".total-project-cost-field").text(formatCurrency(project.total_project_cost));
        $("#total-professional-fees-field").text(formatCurrency(project.total_professional_fees));
        $(".total-construction-costs-field").text(formatCurrency(project.total_construction_costs));
        $(".variation-orders-field").text(formatCurrency(project.variation_orders));
        $("#expenditure-from-previous-years-professional-fees-field").text(formatCurrency(project.expenditure_from_previous_years_professional_fees));
        $(".expenditure-from-previous-years-construction-costs-field").text(formatCurrency(project.expenditure_from_previous_years_construction_costs));
        $(".expenditure-from-previous-years-total-field").text(formatCurrency(project.expenditure_from_previous_years_total));
        $(".project-expenditure-total-field").text(formatCurrency(project.project_expenditure_total));
        $(".main-appropriation-professional-fees-field").text(formatCurrency(project.main_appropriation_professional_fees));
        $(".main-appropriation-construction-costs-field").text(formatCurrency(project.main_appropriation_construction_costs));
        $(".main-appropriation-total-field").text(formatCurrency(project.main_appropriation_total));
        $("#actual-expenditure-q1-field").text(formatCurrency(project.actual_expenditure_q1));
        $("#actual-expenditure-q2-field").text(formatCurrency(project.actual_expenditure_q2));
        $("#actual-expenditure-q3-field").text(formatCurrency(project.actual_expenditure_q3));
        $("#actual-expenditure-q4-field").text(formatCurrency(project.actual_expenditure_q4));

        // Maps and visualisations
        $(".embed-container").css("background-color", "#e1e1e1");

        if (project.latitude !== null & project.longitude !== null) {
            var locationMap = initPointMap(project.latitude, project.longitude);
            var marker = L.marker([project.latitude, project.longitude]).addTo(locationMap);

        }

        $.get("https://mapit.code4sa.org/area/MDB:" + provinceCode[project.province] + "/geometry")
            .done(function(response) {
                var muniMap = initMuniMap(response.centre_lat, response.centre_lon);

                addProvinceToMap(muniMap, project.province);

                if (project.district_municipality === project.local_municipality
                    & project.district_municipality != null) {
                    addMuniToMap(muniMap, project.province, "Metro Municipality", project.local_municipality);
                } else {
                    if (project.district_municipality != null)
                        addMuniToMap(muniMap, project.province, "District Municipality", project.district_municipality);
                    if (project.local_municipality != null)
                        addMuniToMap(muniMap, project.province, "Local Municipality", project.local_municipality);
                }
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
                console.error(jqXHR, textStatus, errorThrown);
            });
    }  // end project page

    if ($("#Infrastructure-Search-Input").length) {

        /** Get templates of dynamically inserted elements **/

        var resultRowTemplate = $("#result-list-container .narrow-card_wrapper:first").clone();
        resultRowTemplate.find(".narrow-card_icon").remove();

        var dropdownItemTemplate = $("#province-dropdown * .dropdown-link:first");
        dropdownItemTemplate.find(".search-status").remove();
        dropdownItemTemplate.find(".search-dropdown_label").text("");
        dropdownItemTemplate.find(".search-dropdown_value").text("");

        $("#map").empty();

        /** initial page state **/
        var searchState = {
            baseLocation: "/api/v1/infrastructure-projects/provincial/search/",
            facetsLocation: "/api/v1/infrastructure-projects/provincial/search/facets/",
            params: new URLSearchParams(),
            selectedFacets: {},
            map: L.map("map").setView([-30.5595, 22.9375], 4),
            markers: L.markerClusterGroup(),
            noResultsMessage: $("#result-list-container * .w-dyn-empty"),
            loadingSpinner: $(".loading-spinner"),
            facetsRequest: null,
            mapPointsRequest: null,
        };
        createTileLayer().addTo(searchState.map);
        searchState.map.addLayer(searchState.markers);

        var facetPlurals = {
            province: "provinces",
            department: "departments",
            status: "project statuses",
            primary_funding_source: "funding sources",
        };

        function updateFreeTextParam() {
            searchState.params.set("q", $("#Infrastructure-Search-Input").val());
        }

        function updateFacetParam() {
            searchState.params.delete("selected_facets");
            for (fieldName in searchState.selectedFacets) {
                var paramValue = fieldName + "_exact:" + searchState.selectedFacets[fieldName];
                searchState.params.append("selected_facets", paramValue);
            }
        }

        function buildPagedSearchURL() {
            updateFreeTextParam();
            updateFacetParam();
            return searchState.facetsLocation + "?" + searchState.params.toString();
        }

        function buildAllCoordinatesSearchURL() {
            var params = new URLSearchParams()
            params.set("q", $("#Infrastructure-Search-Input").val());
            for (fieldName in searchState.selectedFacets) {
                params.set(fieldName, searchState.selectedFacets[fieldName])
            }
            params.set("fields", "url_path,name,latitude,longitude");
            params.set("limit", "1000");
            return searchState.baseLocation + "?" + params.toString();
        }

        function resetResults() {
            $("#num-matching-projects-field").text("");
            $("#result-list-container .narrow-card_wrapper").remove()
            resetDropdown("#province-dropdown");
            resetDropdown("#department-dropdown");
            resetDropdown("#status-dropdown");
            resetDropdown("#primary-funding-source-dropdown");
            searchState.noResultsMessage.hide();
        }

        function triggerSearch() {
            if (searchState.facetsRequest !== null)
                searchState.facetsRequest.abort();
            searchState.facetsRequest = $.get(buildPagedSearchURL())
                .done(function(response) {
                    resetResults();
                    showResults(response);
                })
                .fail(function(jqXHR, textStatus, errorThrown) {
                    if (textStatus !== "abort") {
                        alert("Something went wrong when searching. Please try again.");
                        console.error( jqXHR, textStatus, errorThrown );
                    }
                });
            resetMapPoints();
            getMapPoints(buildAllCoordinatesSearchURL());
        }

        function getMapPoints(url) {
            searchState.loadingSpinner.show();
            if (searchState.mapPointsRequest !== null)
                searchState.mapPointsRequest.abort();
            searchState.mapPointsRequest = $.get(url)
                .done(function(response) {
                    addMapPoints(response);
                    if (response.next) {
                        getMapPoints(response.next);
                    } else {
                        searchState.loadingSpinner.hide();
                    }
                })
                .fail(function(jqXHR, textStatus, errorThrown) {
                    if (textStatus !== "abort") {
                        alert("Something went wrong when loading map data. Please try again.");
                        console.error( jqXHR, textStatus, errorThrown );
                    }
                });
        }

        function showResults(response) {
            $("#num-matching-projects-field").text(response.objects.count);
            updateDropdown("#province-dropdown", response.fields, "province");
            updateDropdown("#department-dropdown", response.fields, "department");
            updateDropdown("#status-dropdown", response.fields, "status");
            updateDropdown("#primary-funding-source-dropdown", response.fields, "primary_funding_source");

            if (response.objects.results.length) {
                searchState.noResultsMessage.hide();
                response.objects.results.forEach(function(project) {
                    var resultItem = resultRowTemplate.clone();
                    resultItem.attr("href", project.url_path);
                    resultItem.find(".narrow-card_title").text(project.name);
                    resultItem.find(".narrow-card_middle-column:first").text(project.status);
                    resultItem.find(".narrow-card_middle-column:last").text(project.estimated_completion_date);
                    resultItem.find(".narrow-card_last-column").text(formatCurrency(project.total_project_cost));
                    $("#result-list-container").append(resultItem);
                });
            } else {
                searchState.noResultsMessage.show();
            }
        }

        function resetMapPoints() {
            searchState.markers.clearLayers();
        }

        function addMapPoints(response) {
            var markers = [];
            response.results.forEach(function(project) {
                if (! project.latitude || ! project.longitude)
                    return;

                var latitude = parseFloat(project.latitude);
                if (latitude < -34.5916 || latitude > -21.783733) {
                    console.log("Ignoring latitude " + latitude);
                    return;
                }

                var longitude = parseFloat(project.longitude);
                if (longitude < 14.206737 || longitude > 33.074960) {
                    console.log("Ignoring longitude " + longitude);
                    return;
                }

                var marker = L.marker([latitude, longitude])
                    .bindPopup(project.name + '<br><a target="_blank" href="' +
                               project.url_path + '">Jump to project</a>');
                markers.push(marker);
            });
            if (markers.length) {
                searchState.markers.addLayers(markers);
                searchState.map.fitBounds(searchState.markers.getBounds());
            }
        }

        function resetDropdown(selector) {
            $(selector).find(".text-block").text("");
            $(selector).find(".dropdown-link").remove();
        }

        function getSelectedOption(fieldName) {
            return searchState.selectedFacets[fieldName];
        }

        function updateDropdown(selector, fields, fieldName) {
            var container = $(selector);
            var optionContainer = container.find(".chart-dropdown_list");

            var selectedOption = getSelectedOption(fieldName);
            if (typeof(selectedOption) == "undefined") {
                container.find(".text-block").text("All " + facetPlurals[fieldName]);
            } else {
                container.find(".text-block").text(selectedOption);
                // Add "clear filter" option
                optionElement = dropdownItemTemplate.clone();
                optionElement.find(".search-dropdown_label").text("All " + facetPlurals[fieldName]);
                optionElement.click(function() {
                    delete searchState.selectedFacets[fieldName];
                    optionContainer.removeClass("w--open");
                    triggerSearch();
                });
                optionContainer.append(optionElement);
            }

            var options = fields[fieldName];
            fields[fieldName].forEach(function (option) {
                optionElement = dropdownItemTemplate.clone();
                optionElement.find(".search-dropdown_label").text(option.text);
                if (option.count) {
                    optionElement.find(".search-dropdown_value").text("(" + option.count + ")");
                }
                optionElement.click(function() {
                    searchState.selectedFacets[fieldName] = option.text;
                    optionContainer.removeClass("w--open");
                    triggerSearch();
                });
                optionContainer.append(optionElement);
            });
        }


        /** Set up search triggering events **/

        $("#Infrastructure-Search-Input").keypress(function (e) {
            var key = e.which;
            if (key == 13) {  // the enter key code
                triggerSearch();
            }
        });
        $("#Search-Button").on("click", triggerSearch);


        /** Search on page load **/

        resetResults();
        triggerSearch()

    } // end search page

})();
