-- Define a function to format and write data to a CSV file
function write_to_csv(dt, mode, summary, latency)
    local file = io.open(dt .. "-" .. mode .. ".csv", "a")
    io.output(file)

    -- Define the CSV header if it doesn't exist
    if file:seek("end") == 0 then
        io.write("requests,duration,bytes_in_mb,requests_per_second,transfer_per_second,")
        io.write("latency_min,latency_max,latency_mean,latency_stdev\n")
    end

    -- Calculate and write the data
    local requests = summary.requests
    local duration = summary.duration
    local bytes = summary.bytes
    local rps = (requests / duration) * 1e6
    local throughput = (bytes / duration)
    local min_latency = latency.min
    local max_latency = latency.max
    local mean_latency = latency.mean
    local stdev_latency = latency.stdev

    io.write(requests .. ",")
    io.write(duration .. ",")
    io.write(bytes .. ",")
    io.write(string.format("%.2f", rps) .. ",")
    io.write(string.format("%.2f", throughput) .. ",")
    io.write(min_latency .. ",")
    io.write(max_latency .. ",")
    io.write(string.format("%.2f", mean_latency) .. ",")
    io.write(string.format("%.2f", stdev_latency) .. "\n")

    io.close(file)
end

-- Call the function when the summary is available
done = function(summary, latency, requests)
    local dt = os.getenv("dt")
    local mode = os.getenv("mode")
    write_to_csv(dt, mode, summary, latency)
end

